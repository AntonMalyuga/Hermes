import testit
from dataclasses import dataclass, field
from page import Page
from locator import Locator, Select, Input


class ComponentOpenPIRAndSMRForm(Page):
    name = 'Редактировать объемы ПИР/СМР B2C'

    _LOCATOR_BUTTON = f'//a[contains(text(),"{name}")]'

    @classmethod
    def open_form(cls):
        with testit.step(f'Открыть форму "{cls.name}"'):
            Page.wait_reload_page()
            Locator(cls._LOCATOR_BUTTON).click()
