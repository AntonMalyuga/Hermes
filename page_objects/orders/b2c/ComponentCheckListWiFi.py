import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select


class ComponentCheckListWiFi(Order):
    _LOCATOR_GROUP = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]')
    _LOCATOR_COMPONENT_COLLAPSED_MENU = (By.XPATH,
                                         '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//b[text()="Wi-Fi"]/ancestor::div[2]//div[@data-toggle = "collapse"]')
    _LOCATOR_COMPONENT_EDIT_BUTTON = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//form[@action = "https://hermes-test.rt.ru/b2c/checklist/save/wifi"]//button[@class="btn btn-info js--b2c-checklist-form-editor"]')
    _LOCATOR_COMPONENT_SELECT_ITEM = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//form[@class = "form-horizontal js--load-element"]//label[text() = "Статья затрат"]/ancestor::div[1]//select[@class = "form-control input-sm"]')
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = (By.XPATH,
                                        '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//div[@id[contains(., "collapseChecklist-wifi")]]//div[@class = "btn-group btn-group-sm"]//button[@class = "btn btn-primary"]')

    def open_drop_down_panel(self):
        self.find_element(locator=self._LOCATOR_COMPONENT_COLLAPSED_MENU).click()

    def push_edit_button(self):
        self.find_element(locator=self._LOCATOR_COMPONENT_EDIT_BUTTON).click()

    def select_dropdown_panel(self, value):
        select = Select(self.find_element(locator=self._LOCATOR_COMPONENT_SELECT_ITEM))
        select.select_by_value(value)

    def push_submit_button(self):
        self.find_element(locator=self._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)

    def add_cost_wifi(self, value: str):
        self.check_loader()
        self.move_to_group()
        self.open_drop_down_panel()
        self.push_edit_button()
        self.select_dropdown_panel(value)
        self.push_submit_button()
