from page import Page
from locator import Locator, Input, CheckBox, Select
import time
import re

import testit


class FormB2BTransferWorkGPH(Page):
    name = 'B2B: Выбор работ ГПХ'
    path = 'aggregator/works/'

    _LOCATOR_CHECKBOX_TRANSFER_GPH = '//form[contains(@action,"works")]//input[@type="checkbox"]//following::label[1]'
    _LOCATOR_BTN_SAVE = '//form[contains(@action,"works")]//button[@type="submit"]'
    _LOCATOR_DIV_CHECK_CHANGES = '//div[@class="alert alert-success alert-dismissable"]'
    _LOCATOR_ALERT_TRANSFER_WORK_IN_GPH = '//pre[contains(text(), "Перенесено работ из строительной заявки")]/strong'
    _LOCATOR_ALERT_TRANSFER_WORK_IN_CONSTRUCTION_ORDER = '//span[contains(text(), "Перенесено работ из заявки")]/strong'
    _LOCATOR_ALERT_CREATE_GPH = '//span[contains(text(), "Заявка на ГПХ")]'

    @classmethod
    def open_form_by_order(cls, order_id: int):
        with testit.step(f'Открыть экранную форму по заявке {order_id}'):
            cls.open_with_path(f'{cls.path}{order_id}')

    @classmethod
    def get_all_switch(cls) -> list[CheckBox]:
        with testit.step('Получить все работы'):
            return CheckBox(cls._LOCATOR_CHECKBOX_TRANSFER_GPH).all

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
    @testit.step('Включение всех работ в строительную заявку')
    def set_all_works_construction_order(cls):
        for switch in cls.get_all_switch():
            if switch.is_checked():
                switch.click()

    @classmethod
    @testit.step('Проверить, что все работы перенесены в схему строительная заявка')
    def check_is_all_work_construction_order(cls):
        for switch in cls.get_all_switch():
            if switch.is_checked():
                return False

    @classmethod
    @testit.step('Включение всех работ в заявку ГПХ')
    def set_all_works_gph(cls):
        for switch in cls.get_all_switch():
            if not (switch.is_checked()):
                switch.click()

    @classmethod
    @testit.step('Проверить, что все работы перенесены в схему ГПХ')
    def check_is_all_work_gph(cls):
        for switch in cls.get_all_switch():
            if not (switch.is_checked()):
                return False

    @classmethod
    @testit.step('Посчитать количество работ')
    def get_cnt_all_work(cls):
        return len(cls.get_all_switch())

    @classmethod
    @testit.step('Получить количество перенесённых работ в заявку ГПХ')
    def get_cnt_work_transfer_in_gph_by_alert(cls) -> int:
        return int(Locator(cls._LOCATOR_ALERT_TRANSFER_WORK_IN_GPH).text)

    @classmethod
    @testit.step('Получить количество перенесённых работ в строительную заявку')
    def get_cnt_work_transfer_in_gph_by_construction_order(cls) -> int:
        return int(Locator(cls._LOCATOR_ALERT_TRANSFER_WORK_IN_CONSTRUCTION_ORDER).text)

    @classmethod
    @testit.step('Получить номер заявки ГПХ')
    def get_number_create_order_gph(cls) -> int:
        alert = Locator(cls._LOCATOR_ALERT_CREATE_GPH).text
        return int(re.findall("\d+", alert)[0])
