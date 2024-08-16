from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentB2CChangeWorkPIRAndSMR(Page):
    name = 'B2C: Редактировать объекмы работы ПИР/СМР'

    _LOCATOR_BUTTON_FORM_WORK = 'a[href*="works_volumes"]'

    def open_form_work(cls):
        with testit.step(f'Открыть форму "{cls.name}"'):
            Locator(cls._LOCATOR_BUTTON_FORM_WORK).click()
