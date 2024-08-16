import time
import testit
from page import Page
from locator import Locator, Input
from pathlib import Path


class ComponentNumberDSOFU(Page):
    name = 'B2C: Номер ДС ОФУ'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//div[@class = "panel-heading binding-flag"]'
    _LOCATOR_EDIT_GLYF = '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//a[@class = "js--load-element"]'
    _LOCATOR_IDENTIFY = '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//input[@title = "идентификатор ДС ОФУ R12"]'
    _LOCATOR_SUBMIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//button[@type = "submit"]'

    @classmethod
    def push_glyf(cls):
        with testit.step(f'Нажать иконку открытия формы редактирования'):
            Locator(cls._LOCATOR_EDIT_GLYF).click()

    @classmethod
    def set_identify_kode(cls, kode):
        with testit.step(f'Ввести идентификационный код "{kode}"'):
            Input(cls._LOCATOR_IDENTIFY).input(kode)

    @classmethod
    def push_submit(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_SUBMIT_BUTTON).click()

    @classmethod
    def add_DSOFU(cls, code: int):
        with testit.step(f'Добавить ДСОФУ с кодом "{code}"'):
            cls.push_glyf()
            cls.set_identify_kode(code)
            cls.push_submit()
