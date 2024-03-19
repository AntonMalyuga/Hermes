import time

from exception import exception
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ComponentTypeProject(Order):
    _LOCATOR_GROUP = (
        By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]')
    _LOCATOR_EDIT_FORM_BUTTON = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "agg-container--limited-height"]//a[@title = "Редактировать"]')
    _LOCATOR_SELECT_TYPE_FIELD = (By.XPATH,
                                  '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//select[@name = "project_type"]')
    _LOCATOR_SELECT_TYPE_SUBMIT_BUTTON = (By.XPATH,
                                          '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "input-group-btn"]//button[@type = "submit"]')

    def push_edit_form_button(self):
        self.find_element(locator=self._LOCATOR_EDIT_FORM_BUTTON).click()

    def fill_select_type_field(self, value):
        select = Select(self.find_element(locator=self._LOCATOR_SELECT_TYPE_FIELD))
        select.select_by_visible_text(value)

    def push_submit_button(self):
        self.find_element(locator=self._LOCATOR_SELECT_TYPE_SUBMIT_BUTTON).click()

    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)

    def check_type_project(self, value: str):
        self.check_loader()
        self.move_to_group()
        self.push_edit_form_button()
        self.fill_select_type_field(value)
        self.push_submit_button()

