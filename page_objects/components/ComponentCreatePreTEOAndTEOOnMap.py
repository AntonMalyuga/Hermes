from dataclasses import dataclass, field
from page import Page
from locator import Locator, Select, Input
import testit


class ComponentCreatePreTEOAndTEOOnMap(Page):
    name = 'Создание предТЭО и ТЭО на карте'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_OPEN_MAP = f'{_GROUP}//a[contains(., "Создание предТЭО и ТЭО на карте")]'

    @classmethod
    def open_form(cls):
        with testit.step(f'Открыть форму создания проекта'):
            Locator(cls._LOCATOR_OPEN_MAP).click()
