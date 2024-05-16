from abc import ABCMeta, abstractmethod
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
# from page_objects.components.InterfaceComponent import InterfaceComponent


class Component(BasePage):

    name: str
    group: str

    _SELECTOR_GROUP = f'//div[@class="panel panel-material"]//span[contains(., "")]/ancestor::div[2]'
    _LOCATOR_GROUP = (By.XPATH, _SELECTOR_GROUP)

    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)
