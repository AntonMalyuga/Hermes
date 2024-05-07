import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
import testit


class ComponentConnectionParameters(Order):
    _LOCATOR_GROUP = (
        By.XPATH, '//span[contains(., "Параметры подключения")]')
    _LOCATOR_PARAMETERS_BUTTON = (
        By.XPATH,
        '//span[contains(., "Параметры подключения")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]')
    _LOCATOR_ORGANIZATION_WAY = (By.XPATH, '//select[@name = "last_inch_method"]')
    _LOCATOR_COORDINATION = (By.XPATH, '//textarea[@name = "approval_details"]')
    _LOCATOR_SPECIAL_CONDITIONS = (By.XPATH, '//textarea[@name = "special_conditions"]')
    _LOCATOR_CROSSING = (By.XPATH, '//select[@name = "lm_crossing"]')
    _LOCATOR_LAST_MILE = (By.XPATH, '//select[@name = "last_mile_method"]')
    _LOCATOR_NETWORK_PATH = (By.XPATH, '//select[@name= "crm_network_path"]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH,
                              '//span[contains(., "Информация о подключении")]/ancestor::div[2]//button[@class[not(contains(., "disable-after-click"))]]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def push_edit_form_button(self):
        with testit.step(f'Открыть форму редактирования'):
            self.find_element(locator=self._LOCATOR_PARAMETERS_BUTTON).click()

    def fill_organization_way_field(self, value):
        with testit.step(f'Заполнить селектовую форму со значением нового способа организации "{value}"'):
            select = Select(self.find_element(locator=self._LOCATOR_ORGANIZATION_WAY))
            select.select_by_visible_text(value)

    def fill_coordination(self, coordination):
        with testit.step(f'Установить тип согласования {coordination}'):
            self.find_element(locator=self._LOCATOR_COORDINATION).clear()
            self.find_element(locator=self._LOCATOR_COORDINATION).send_keys(coordination)

    def fill_special_conditions(self, conditions):
        with testit.step(f'Установить особые условия {conditions}'):
            self.find_element(locator=self._LOCATOR_SPECIAL_CONDITIONS).clear()
            self.find_element(locator=self._LOCATOR_SPECIAL_CONDITIONS).send_keys(conditions)

    def fill_crossing(self, crossing):
        with testit.step(f'Заполнить селектовую форму со значением нового способа кроссировки "{crossing}"'):
            select = Select(self.find_element(locator=self._LOCATOR_CROSSING))
            select.select_by_visible_text(crossing)

    def fill_last_mile(self, last_mile):
        with testit.step(f'Заполнить селектовую форму "уровень организации last mile" "{last_mile}"'):
            select = Select(self.find_element(locator=self._LOCATOR_LAST_MILE))
            select.select_by_visible_text(last_mile)

    def fill_network_path(self, network):
        with testit.step(f'Заполнить селектовую форму "задействованные участки сети" "{network}"'):
            select = Select(self.find_element(locator=self._LOCATOR_NETWORK_PATH))
            select.select_by_visible_text(network)

    def push_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    def change_connection_parameters(self, value: str, coordination: str, conditions: str, crossing: str,
                                     last_mile: str, network: str):
        with testit.step(f'Изменить параметры подключения'):
            self.move_to_group()
            self.push_edit_form_button()
            self.check_loader()
            self.fill_organization_way_field(value)
            self.fill_coordination(coordination)
            self.fill_special_conditions(conditions)
            self.fill_crossing(crossing)
            self.fill_last_mile(last_mile)
            self.fill_network_path(network)
            self.push_submit_button()
            time.sleep(10)
