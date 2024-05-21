from __future__ import annotations
from playwright.sync_api import Locator as PlaywrightLocator
from driver import Driver

DEFAULT_TIMEOUT = 5_000  # ms


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
                f"Element {self.name} with xpath={self.block_xpath + self.xpath} is not visible")


class Input(Locator):
    def input(self, string: str):
        self._use_current_page_context()
        self.webelement.first.fill(string, timeout=DEFAULT_TIMEOUT)

    def value(self) -> str:
        self._use_current_page_context()
        return self.webelement.first.input_value(timeout=DEFAULT_TIMEOUT)
