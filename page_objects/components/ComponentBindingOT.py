from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentBindingOT(Page):
    name = 'Привязка ОТ'

    _LOCATOR_GROUP = '//span[contains(., "Параметры подключения")]'
    _LOCATOR_BINDING_BUTTON = '//a[@title = "Привязка ОТ"]'
    _LOCATOR_REFERENCE_POINT = '//select[@name= "cluster_node"]'
    _LOCATOR_SUBMIT_BUTTON = '//button[text() = "Привязать"]'

    @classmethod
    def push_edit_form_button(cls):
        with testit.step(f'Открыть форму редактирования'):
            Locator(cls._LOCATOR_BINDING_BUTTON).click()

    @classmethod
    def set_reference_point(cls, value):
        with testit.step(f'Заполнить селектовую форму со значением опорной точки "{value}"'):
            Select(cls._LOCATOR_REFERENCE_POINT)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            Locator(cls._LOCATOR_SUBMIT_BUTTON).click()

    @classmethod
    def change_binding_ot(cls, value: str):
        with testit.step(f'Изменить привязку ОТ'):
            cls.push_edit_form_button()
            cls.set_reference_point(value)
            cls.push_submit_button()
