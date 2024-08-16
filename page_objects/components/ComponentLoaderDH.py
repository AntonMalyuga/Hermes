import testit
from page import Page
from locator import Locator, Select, Input
from pathlib import Path


class ComponentLoaderDH(Page):
    name = 'B2C: Загрузчик ДХ'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]'
    _LOCATOR_YANDEX_LINK = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "yandex_constructor_link"]'
    _LOCATOR_SET_FILE_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@class= "form-control input-sm js--extract-file-name-on-change"]'
    _LOCATOR_LOAD_FILE_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//div[@class = "form-group"]//button[@type= "submit"]'

    @classmethod
    def set_yandex_link(cls, link):
        with testit.step(f'Добавить ссылку на Яндекс карты "{link}" для компонента загрузчик ДХ'):
            Input(cls._LOCATOR_YANDEX_LINK).input(link)

    @classmethod
    def set_file_path(cls, file_name: str):
        with testit.step(f'Добавить путь файла "{file_name}" для компонента загрузчик ДХ'):
            file_path = str(Path(__file__).resolve().parents[1].joinpath('b2c').joinpath('files').joinpath(file_name))
            Input(cls._LOCATOR_SET_FILE_BUTTON).input(file_path)

    @classmethod
    def push_set_file_button(cls):
        with testit.step(f'Нажать кнопку добавить файл'):
            Locator(cls._LOCATOR_LOAD_FILE_BUTTON).click()

    @classmethod
    def add_dh(cls, link: str, file_name: str):
        with testit.step(f'Добавить загрузку ДХ по ссылке "{link}" и именем файла "{file_name}"'):
            cls.set_yandex_link(link)
            cls.set_file_path(file_name)
            cls.push_set_file_button()
