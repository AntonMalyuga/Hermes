from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentAdressParameters(Page):
    name = 'B2C: Параметры адреса'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]'
    _LOCATOR_EDIT_FORM = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]'
    _LOCATOR_ABONENT_COUNT = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "active_subscribers_count"]'
    _LOCATOR_SET_ABONENTS_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//form[@class = "form js--load-element"]//button[@type= "submit"]'
    _LOCATOR_YANDEX_LINK = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "yandex_constructor_link"]'
    _LOCATOR_SET_FILE_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@class= "form-control input-sm js--extract-file-name-on-change"]'
    _LOCATOR_LOAD_FILE_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//div[@class = "form-group"]//button[@type= "submit"]'

    @classmethod
    def push_edit_form(cls):
        with testit.step(f'Открыть редактирование параметров адреса', 'Форма редактирования открыта'):
            Locator(cls._LOCATOR_EDIT_FORM).click()

    @classmethod
    def set_abonents(cls, abonents):
        with testit.step(f'Set abonent {abonents}'):
            Input(cls._LOCATOR_ABONENT_COUNT).input(abonents)

    @classmethod
    def push_set_abonents_button(cls):
        with testit.step(f'Нажать кнопку сохранения параметров адреса', 'Сохранение успешно'):
            Locator(cls._LOCATOR_SET_ABONENTS_BUTTON).click()

    @classmethod
    @testit.step('Add abbonents')
    def add_abonents(cls, abonents: int):
        with testit.step(f'Добавить абонентов "{abonents}"'):
            cls.push_edit_form()
            cls.set_abonents(abonents)
            cls.push_set_abonents_button()
