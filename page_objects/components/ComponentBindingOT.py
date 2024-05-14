import time

from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
import testit


class ComponentBindingOT(Order):

    name = 'Привязка ОТ'

    _LOCATOR_GROUP = (
        By.XPATH, '//span[contains(., "Параметры подключения")]')
    _LOCATOR_BINDING_BUTTON = (
        By.XPATH,
        '//a[@title = "Привязка ОТ"]')
    _LOCATOR_REFERENCE_POINT = (By.XPATH, '//select[@name= "cluster_node"]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH, '//button[text() = "Привязать"]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def push_edit_form_button(self):
        with testit.step(f'Открыть форму редактирования'):
            self.find_element(locator=self._LOCATOR_BINDING_BUTTON).click()

    def fill_reference_point(self, value):
        with testit.step(f'Заполнить селектовую форму со значением опорной точки "{value}"'):
            select = Select(self.find_element(locator=self._LOCATOR_REFERENCE_POINT))
            select.select_by_visible_text(value)

    def push_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    def change_binding_ot(self, value: str):
        with testit.step(f'Изменить привязку ОТ'):
            self.move_to_group()
            self.push_edit_form_button()
            self.check_loader()
            self.fill_reference_point(value)
            self.push_submit_button()
