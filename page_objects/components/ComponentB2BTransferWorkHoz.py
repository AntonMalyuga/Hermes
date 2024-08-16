import time

from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentB2BTransferWorkHoz(Page):
    name = 'B2B: Хоз. способ'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_BUTTON_HOZ = f'{_GROUP}//a[text()="Хоз. способ"]'

    @classmethod
    def open_form_transfer_hoz_work(cls):
        with testit.step(f'Открыть форму "{cls.name}"'):
            Locator(cls._LOCATOR_BUTTON_HOZ).click()
