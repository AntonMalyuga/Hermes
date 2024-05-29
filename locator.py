from __future__ import annotations

import time

from playwright.sync_api import Locator as PlaywrightLocator
from driver import Driver

DEFAULT_TIMEOUT = 30000  # ms


class Locator:
    name: str = ""
    xpath: str = None
    block_xpath: str = ""
    parent: PlaywrightLocator = None
    webelement: PlaywrightLocator = None

    def __init__(self, xpath: str, name: str = ''):
        self.xpath = xpath
        self.name = name

    def _use_current_page_context(self):
        if self.parent:
            self.webelement = self.parent.locator(self.block_xpath + self.xpath)
        else:
            self.webelement = Driver().page.locator(self.block_xpath + self.xpath)

    def click(self, wait_for_new_page: bool = False, wait_for_new_tab: bool = False):
        self._use_current_page_context()

        if wait_for_new_tab:
            with Driver().browser.contexts[0].expect_page() as _:
                self.webelement.first.click(timeout=DEFAULT_TIMEOUT)
            Driver().switch_to_tab(-1)
        else:
            self.webelement.first.click(timeout=DEFAULT_TIMEOUT)

        if wait_for_new_page:
            Driver().page.wait_for_load_state('domcontentloaded')

    @property
    def text(self) -> str:
        self._use_current_page_context()
        return "".join(self.webelement.first.all_text_contents())

    def is_on_page(self) -> bool:
        self._use_current_page_context()
        self.wait_for_displayed(timeout=DEFAULT_TIMEOUT)
        return self.webelement.first.is_visible()

    def get_attribute(self, attribute) -> str:
        self._use_current_page_context()
        return self.webelement.first.get_attribute(attribute, timeout=DEFAULT_TIMEOUT)

    def wait_for_displayed(self, timeout=DEFAULT_TIMEOUT):
        self._use_current_page_context()
        try:
            self.webelement.first.wait_for(timeout=timeout, state="visible")
        except:
            raise Exception(
                f"Элемента {self.name} по xpath={self.block_xpath + self.xpath} не видно на странице")

    def press(self, keys_command: str = '', timeout=DEFAULT_TIMEOUT):
        self._use_current_page_context()
        self.webelement.first.press(keys_command)

    def press_sequentially(self, text: str):
        self._use_current_page_context()
        self.webelement.first.press_sequentially(text)

    def wait_attached(self, timeout=DEFAULT_TIMEOUT):
        self._use_current_page_context()
        try:
            self.webelement.first.wait_for(timeout=timeout, state="attached")
        except:
            raise Exception(
                f"Элемента {self.name} по xpath={self.block_xpath + self.xpath} не найдено в DOM")

    @property
    def count(self, timeout=DEFAULT_TIMEOUT):
        self._use_current_page_context()
        return self.webelement.count()


class Input(Locator):
    def input(self, string: str):
        self._use_current_page_context()
        self.webelement.first.fill(string, timeout=DEFAULT_TIMEOUT)

    def value(self) -> str:
        self._use_current_page_context()
        return self.webelement.first.input_value(timeout=DEFAULT_TIMEOUT)


class CheckBox(Locator):
    def checked(self):
        self._use_current_page_context()
        return self.webelement.first.set_checked(timeout=DEFAULT_TIMEOUT, checked=True)

    def unchecked(self):
        self._use_current_page_context()
        return self.webelement.first.set_checked(timeout=DEFAULT_TIMEOUT, checked=False)


class Select(Locator):
    def ajax_option(self, string: str):
        self._use_current_page_context()
        Locator(f'{self.xpath}//following::div[1]').click()
        Input(f'{self.xpath}//following::div[1]//input[@type="text"]').input(string)
        Locator(f'{self.xpath}//following::div[1]//span[contains(., "{string}")]').click()

    def option(self, string: str):
        self._use_current_page_context()
        self.webelement.first.select_option(string)

    def index(self, index: int):
        self._use_current_page_context()
        self.webelement.select_option(index=index, timeout=DEFAULT_TIMEOUT)

    def option_by_index(self, index: int):
        self._use_current_page_context()
        self.webelement.first.select_option(timeout=DEFAULT_TIMEOUT, index=index)
