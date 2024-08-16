import time

from page import Page
from locator import Locator, Select, Input
import testit


class ComponentConnectionParameters(Page):

    name = 'Параметры подключения'

    _LOCATOR_GROUP = '//span[contains(., "Параметры подключения")]'
    _LOCATOR_PARAMETERS_BUTTON = '//span[contains(., "Параметры подключения")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]'
    _LOCATOR_ORGANIZATION_WAY = '//select[@name = "last_inch_method"]'
    _LOCATOR_COORDINATION = '//textarea[@name = "approval_details"]'
    _LOCATOR_SPECIAL_CONDITIONS = '//textarea[@name = "special_conditions"]'
    _LOCATOR_CROSSING = '//select[@name = "lm_crossing"]'
    _LOCATOR_LAST_MILE = '//select[@name = "last_mile_method"]'
    _LOCATOR_NETWORK_PATH = '//select[@name= "crm_network_path"]'
    _LOCATOR_SUBMIT_BUTTON = '//span[contains(., "Информация о подключении")]/ancestor::div[2]//button[@class[not(contains(., "disable-after-click"))]]'


    @classmethod
    def push_edit_form_button(cls):
        with testit.step(f'Открыть форму редактирования'):
            Locator(cls._LOCATOR_PARAMETERS_BUTTON).click()

    @classmethod
    def fill_organization_way_field(cls, value):
        with testit.step(f'Заполнить селектовую форму со значением нового способа организации "{value}"'):
            select = Select(cls._LOCATOR_ORGANIZATION_WAY).option(value)

    @classmethod
    def fill_coordination(cls, coordination):
        with testit.step(f'Установить тип согласования {coordination}'):
            Input(cls._LOCATOR_COORDINATION).input(coordination)

    @classmethod
    def fill_special_conditions(cls, conditions):
        with testit.step(f'Установить особые условия {conditions}'):
            Input(cls._LOCATOR_SPECIAL_CONDITIONS).input(conditions)

    @classmethod
    def fill_crossing(cls, crossing):
        with testit.step(f'Заполнить селектовую форму со значением нового способа кроссировки "{crossing}"'):
            Select(cls._LOCATOR_CROSSING).option(crossing)

    @classmethod
    def fill_last_mile(cls, last_mile):
        with testit.step(f'Заполнить селектовую форму "уровень организации last mile" "{last_mile}"'):
            Select(cls._LOCATOR_LAST_MILE).option(last_mile)

    @classmethod
    def fill_network_path(cls, network):
        with testit.step(f'Заполнить селектовую форму "задействованные участки сети" "{network}"'):
            select = Select(cls._LOCATOR_NETWORK_PATH).option(network)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения параметров', 'Сохранение успешно'):
            Locator(cls._LOCATOR_SUBMIT_BUTTON).click()

    @classmethod
    def change_connection_parameters(cls, value: str, coordination: str, conditions: str, crossing: str,
                                     last_mile: str, network: str):
        with testit.step(f'Изменить параметры подключения'):
            cls.push_edit_form_button()
            cls.fill_organization_way_field(value)
            cls.fill_coordination(coordination)
            cls.fill_special_conditions(conditions)
            cls.fill_crossing(crossing)
            cls.fill_last_mile(last_mile)
            cls.fill_network_path(network)
            cls.push_submit_button()
            time.sleep(10)
