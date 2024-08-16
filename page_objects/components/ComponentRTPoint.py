import time
import testit
from page import Page
from locator import Locator, Select, Input


class ComponentRTPoint(Page):

    name = 'B2B: Точка РТ'

    _LOCATOR_GROUP = '//span[contains(., "Точка РТ")]'
    _LOCATOR_RF_POINT_BUTTON = '//span[contains(., "Точка РТ")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]'
    _LOCATOR_INTERFACE = '//select[@name= "interface"]'
    _LOCATOR_EQUIPMENT = '//textarea[@id= "equipment"]'
    _LOCATOR_SUBMIT_BUTTON = '//textarea[@id= "equipment"]/ancestor::div[2]//button[@type = "submit"]'


    @classmethod
    def push_edit_form_button(cls):
        with testit.step(f'Открыть форму редактирования'):
            Locator(cls._LOCATOR_RF_POINT_BUTTON).click()


    @classmethod
    def fill_interface(cls, interface):
        with testit.step(f'Заполнить селектовую форму со значением нового интерфейса "{interface}"'):
            Select(cls._LOCATOR_INTERFACE).option(interface)


    @classmethod
    def fill_equipment(cls, equipment):
        with testit.step(f'Установить тип оборудования {equipment}'):
            Input(cls._LOCATOR_EQUIPMENT).input(equipment)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            Locator(cls._LOCATOR_SUBMIT_BUTTON).click()

    @classmethod
    def change_rt_point(cls, interface: str, equipment: str):
        with testit.step(f'Изменить параметры подключения'):
            cls.push_edit_form_button()
            cls.fill_interface(interface)
            cls.fill_equipment(equipment)
            cls.push_submit_button()
            time.sleep(10)
