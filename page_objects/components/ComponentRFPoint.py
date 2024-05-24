import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
import testit


class ComponentRFPoint(Order):

    name = 'B2B: Точка РФ'

    _LOCATOR_GROUP = (
        By.XPATH, '//span[contains(., "Точка РФ")]')
    _LOCATOR_RF_POINT_BUTTON = (
        By.XPATH,
        '//span[contains(., "Точка РФ")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]')
    _LOCATOR_INTERFACE = '//select[@name= "interface"]')
    _LOCATOR_EQUIPMENT = '//textarea[@id= "equipment"]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH,
                              '//textarea[@id= "equipment"]/ancestor::div[2]//button[@type = "submit"]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def push_edit_form_button(self):
        with testit.step(f'Открыть форму редактирования'):
            self.find_element(locator=self._LOCATOR_RF_POINT_BUTTON).click()

    def fill_interface(self, interface):
        with testit.step(f'Заполнить селектовую форму со значением нового интерфейса "{interface}"'):
            select = Select(self.find_element(locator=self._LOCATOR_INTERFACE))
            select.select_by_visible_text(interface)

    def fill_equipment(self, equipment):
        with testit.step(f'Установить тип оборудования {equipment}'):
            self.find_element(locator=self._LOCATOR_EQUIPMENT).clear()
            self.find_element(locator=self._LOCATOR_EQUIPMENT).send_keys(equipment)

    def push_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    def change_rf_point(self, interface: str, equipment: str):
        with testit.step(f'Изменить параметры подключения'):
            self.check_loader()
            self.move_to_group()
            self.push_edit_form_button()
            self.check_loader()
            self.fill_interface(interface)
            self.fill_equipment(equipment)
            self.push_submit_button()
            time.sleep(10)
