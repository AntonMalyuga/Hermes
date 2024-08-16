from dataclasses import dataclass, field
from page import Page
from locator import Locator, Select, Input
import testit


class ComponentCreateProjectButton(Page):
    name = 'B2C: Создать строительный проект'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_CREATE_PROJECT_BUTTON = f'{_GROUP}//a[contains(., "Создать строительный проект")]'

    @classmethod
    def confirm(cls):
        with testit.step(f'Открыть форму создания проекта'):
            Locator(cls._LOCATOR_CREATE_PROJECT_BUTTON).click()
