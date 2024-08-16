from page import Page
from locator import Locator, Input, CheckBox, Select

import testit


class FormB2BTransferWorkHoz(Page):
    name = 'B2B: Выбор работ хоз. способом'
    path = 'aggregator/works/'

    _LOCATOR_CHECKBOX_TRANSFER_HOZ = '//form[contains(@action,"works")]//input[@type="checkbox"]//following::label[1]'
    _LOCATOR_BTN_SAVE = '//form[contains(@action,"works")]//button[@type="submit"]'
    _LOCATOR_DIV_CHECK_CHANGES = '//div[@class="alert alert-success alert-dismissable"]'


    @classmethod
    def open_form(cls, order_id: int):
        with testit.step(f'Открыть экранную форму по заявке {order_id}'):
            cls.open_with_path(f'{cls.path}{order_id}')

    @classmethod
    def get_all_switch_hoz(cls) -> list[Locator]:
        with testit.step('Получить все работы'):
            return Locator(cls._LOCATOR_CHECKBOX_TRANSFER_HOZ).all

    @classmethod
    def save(cls):
        with testit.step('Нажать на кнопку сохранения работ'):
            Locator(cls._LOCATOR_BTN_SAVE).click()

    @classmethod
    def check_save_changes(cls) -> bool:
        with testit.step('Проверка успешного переноса работ', 'Работы успешно перенесены'):
            if Locator(cls._LOCATOR_DIV_CHECK_CHANGES).is_on_page():
                return True
            else:
                raise Exception('Работы не перенесены')

    @classmethod
    @testit.step('Включение всех работ')
    def set_all_works_hoz(cls):
        for switch in cls.get_all_switch_hoz():
            switch.click()
        cls.save()
        cls.check_save_changes()
