import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
class ComponentPanelMaterialPart(Order):
    _LOCATOR_GROUP = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]')
    _LOCATOR_COMPONENT_DROPDOWN_MENU = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//select[@class[contains(., "form-control input-medium input-sm change-expenses-monitoring-object")]]')
    _LOCATOR_COMPONENT_OTHER_CAPITAL_COSTS_DROPDOWN = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//div[@id[contains(., "component-otherCapex")]]/div[1]')
    _LOCATOR_OTHER_CAPITAL_EDIT_BUTTON = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//div[@id[contains(., "component-otherCapex")]]//i[@class = "fas fa-edit"]')
    _LOCATOR_COMPONENT_DELETE_STRING = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title= "Удалить"]')
    _LOCATOR_COMPONENT_ADD_STRING = (By.XPATH,
                                     '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title= "Добавить строку"]')
    _LOCATOR_COMPONENT_ADD_EXPENCE_NAME = (By.XPATH,
                                           '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//td[@data-field = "name"]//input[@class = "form-control input-sm"]')
    _LOCATOR_COMPONENT_OBJECT_DROPDOWN = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//select[@class[contains(., "form-control input-sm js--other-capexes-changeOrder")]]')
    _LOCATOR_COMPONENT_ADD_COST = (By.XPATH,
                                   '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//td[@data-field = "cost"]//input[@class = "form-control input-sm"]')
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = (By.XPATH,
                                   '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title = "Сохранить прочие капитальные расходы"]')

    def fill_drop_down_menu(self, value):
        select = Select(self.find_element(locator=self._LOCATOR_COMPONENT_DROPDOWN_MENU))
        select.select_by_value(value)

    def push_open_capital_dropdown(self):
        self.find_element(locator=self._LOCATOR_COMPONENT_OTHER_CAPITAL_COSTS_DROPDOWN).click()

    def push_other_capital_edit_button(self):
        self.find_element(locator=self._LOCATOR_OTHER_CAPITAL_EDIT_BUTTON).click()

    def check_new_string_necessity(self):
        try:
            self.find_element(locator=self._LOCATOR_COMPONENT_DELETE_STRING).click()
            time.sleep(3)
        except TimeoutException:
            self.find_element(locator=self._LOCATOR_COMPONENT_ADD_STRING).click()
            time.sleep(3)
        else:
            self.find_element(locator=self._LOCATOR_COMPONENT_ADD_STRING).click()

    def fill_object_dropdown(self, text):
        select = Select(self.find_element(locator=self._LOCATOR_COMPONENT_OBJECT_DROPDOWN))
        select.select_by_visible_text(text)

    def fill_expence_name(self, name):
        self.find_element(locator=self._LOCATOR_COMPONENT_ADD_EXPENCE_NAME).send_keys(name)

    def fill_cost(self, cost):
        self.find_element(locator=self._LOCATOR_COMPONENT_ADD_COST).send_keys(cost)

    def submit_button_click(self):
        self.find_element(locator=self._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    def add_material_part(self, value: str, name: str, cost: int, text: str):
        self.fill_drop_down_menu(value)
        self.push_open_capital_dropdown()
        self.push_other_capital_edit_button()
        self.check_new_string_necessity()
        self.fill_object_dropdown(text)
        self.fill_expence_name(name)
        self.fill_cost(cost)
        self.submit_button_click()