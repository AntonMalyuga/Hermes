import time
import testit
from page import Page
from locator import Locator, Select, Input


class ComponentLinkSip(Page):
    name = 'B2C: Ссылка на карточку ИП в СИП'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]'
    _LOCATOR_EDIT_FORM_BUTTON_CART = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "clearfix agg-caption"]//a[@title = "Редактировать"]'
    _LOCATOR_B2C_LIP_FIELD = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[2]"]'
    _LOCATOR_B2C_KIP_CORE_FIELD = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[3]"]'
    _LOCATOR_B2C_KIP_KEY_FIELD = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[4]"]'
    _LOCATOR_CART_SUBMIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//form[@class = "form js--load-element"]//button[@type = "submit"]'

    @classmethod
    def push_edit_cart_form_button(cls):
        with testit.step(f'Нажать кнопку редактирования карточки', 'Кнопка нажата'):
            Locator(cls._LOCATOR_EDIT_FORM_BUTTON_CART).click()

    @classmethod
    def change_link_sip(cls, lip, kip, kip_key):
        with testit.step(f'Выбрать ссылку СИП: ЛИП "{lip}", КИП "{kip}" или ключ КИП "{kip_key}"'):
            cls.clean_strings(cls._LOCATOR_B2C_LIP_FIELD)
            cls.clean_strings(cls._LOCATOR_B2C_KIP_CORE_FIELD)
            cls.clean_strings(cls._LOCATOR_B2C_KIP_KEY_FIELD)
            if lip == "" and kip == "" and kip_key == "":
                raise 'Не введены значения'

            if lip != "":
                cls.clean_strings(cls._LOCATOR_B2C_LIP_FIELD)
                cls.insert(cls._LOCATOR_B2C_LIP_FIELD, lip)
            if kip != "":
                cls.clean_strings(cls._LOCATOR_B2C_KIP_CORE_FIELD)
                cls.insert(cls._LOCATOR_B2C_KIP_CORE_FIELD, kip)
            if kip_key != "":
                cls.clean_strings(cls._LOCATOR_B2C_KIP_KEY_FIELD)
                cls.insert(cls._LOCATOR_B2C_KIP_KEY_FIELD, kip_key)

    @classmethod
    def insert(cls, input_locator, value):
        with testit.step(f'Ввести значение "{value}"'):
            Input(input_locator).input(value)

    @classmethod
    def clean_strings(cls, locator):
        with testit.step(f'Очистить строку'):
            Input(locator).input('')

    @classmethod
    def push_cart_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_CART_SUBMIT_BUTTON).click()

    @classmethod
    def add_link_sip(cls, lip: str, kip: str, kip_key: str):
        with testit.step(f'Добавить ссылку СИП: ЛИП "{lip}", КИП "{kip}" или ключ КИП "{kip_key}"'):
            cls.push_edit_cart_form_button()
            cls.change_link_sip(lip, kip, kip_key)
            cls.push_cart_submit_button()
