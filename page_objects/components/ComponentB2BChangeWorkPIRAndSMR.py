import time
from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentB2BChangeWorkPIRAndSMR(Page):
    name = 'B2B: Редактировать объекмы работы ПИР/СМР'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_BUTTON_FORM_WORK = f'{_GROUP}//a[text()="Редактировать объемы ПИР/СМР"]'

    @classmethod
    def open_form_work(cls, order_id: int):
        with testit.step(f'Открыть форму "{cls.name}" по заявке {order_id}'):
            Locator(cls._LOCATOR_BUTTON_FORM_WORK).click()
