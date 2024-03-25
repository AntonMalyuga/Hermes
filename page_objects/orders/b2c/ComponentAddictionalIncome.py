import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class ComponentAdditionalIncome(Order):
    _LOCATOR_GROUP = (
        By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]')
    _LOCATOR_EDIT_FORM_BUTTON = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@title = "Редактировать дополнительные доходы"]')
    _LOCATOR_TABLE_ROWS = (By.XPATH,
                           '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//form[@action[contains(., "additionalIncome")]]//table[@class="b2c-table-component"]/tbody/tr')
    _LOCATOR_DELETE_STRING = (By.XPATH,
                              '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//button[@title = "Удалить доход"]')
    _LOCATOR_CREATE_NEW_STRING = (By.XPATH,
                                  '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@class = "btn btn-default js--b2c-components-add-row"]')
    _LOCATOR_ADD_NAME_STRING = (By.XPATH,
                                '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//input[@class = "form-control input-sm"]')
    _LOCATOR_ADD_INFRASTRUCTURE_TYPE_STRING = (By.XPATH,
                                               '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//select[@class = "form-control input-sm js--fetch-income-types-for-infrastructure"]')
    _LOCATOR_ADD_INCOME_TYPE_STRING = (By.XPATH,
                                       '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//td[@class[contains(., "column")]]//select[@class = "form-control input-sm"]')
    _LOCATOR_ADD_ABONENT_BASE_STRING = (By.XPATH,
                                        '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//select[contains(@name, "subscriberBaseType[1]") ]')
    _LOCATOR_ADD_YEARS_STRING = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//input[@class = "form-control input-sm js--b2c-year-value"]')

    _LOCATOR_SAVE_BUTTON = (By.XPATH,
                            '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@class = "btn btn-primary"]')

    def push_edit_form_button(self):
        self.find_element(locator=self._LOCATOR_EDIT_FORM_BUTTON).click()

    def check_new_string_necessity(self):
        elements = self.find_elements(locator=self._LOCATOR_TABLE_ROWS)
        if len(elements) > 1:
            self.find_element(locator=self._LOCATOR_DELETE_STRING).click()
            self.find_element(locator=self._LOCATOR_CREATE_NEW_STRING).click()
        else:
            self.find_element(locator=self._LOCATOR_CREATE_NEW_STRING).click()

    def fill_name_string(self, name):
        self.find_element(locator=self._LOCATOR_ADD_NAME_STRING).send_keys(name)

    def fill_infrastructure_string(self, infrastructure_type):
        select = Select(self.find_element(locator=self._LOCATOR_ADD_INFRASTRUCTURE_TYPE_STRING))
        select.select_by_visible_text(infrastructure_type)

    def fill_income_string(self, income_type):
        select = Select(self.find_element(locator=self._LOCATOR_ADD_INCOME_TYPE_STRING))
        select.select_by_visible_text(income_type)

    def fill_abonent_string(self, abonent_type):
        select = Select(self.find_element(locator=self._LOCATOR_ADD_ABONENT_BASE_STRING))
        select.select_by_visible_text(abonent_type)

    def fill_years_income(self, value):
        elements = self.find_elements(locator=self._LOCATOR_ADD_YEARS_STRING)

        for element in elements:
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(value)
            time.sleep(1)

    def push_save_button(self):
        self.find_element(locator=self._LOCATOR_SAVE_BUTTON).click()

    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)

    def add_addictional_income(self, name: str, infrastructure_type: str, income_type: str, abonent_type: str,
                               value: int):
        self.check_loader()
        self.move_to_group()
        self.push_edit_form_button()
        self.check_new_string_necessity()
        self.fill_name_string(name)
        self.fill_infrastructure_string(infrastructure_type)
        self.fill_income_string(income_type)
        self.fill_abonent_string(abonent_type)
        self.fill_years_income(value)
        self.push_save_button()
