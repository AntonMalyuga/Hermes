import random
import time

import testit
from locator import Locator
from page import Page


class FormB2BWorkVolume(Page):
    name = 'Редактировать объемы ПИР/СМР B2B'
    path = '/aggregator/volumes/'

    _LOCATOR_BTN_SHOW_ALL_WORKS = '//button[@title="Отобразить все объемы работ"]'
    _LOCATOR_INPUTS_VALUE_ALL_WORKS = '//div[@id="works-tab"]//tbody//tr[not(@class="hidden") and @data-work-type]'
    _LOCATOR_BTN_SAVE_WORKS = '//form[contains(@id, "volumesForm")]//button[contains(text(), "Сохранить")]'
    _LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED = '//div[contains(@id,"volumesFormTab")]/div[@class="alert-success alert"]'
    _LOCATOR_BTN_DELETE_WORKS = '//tr[not(@class="hidden")]//button'

    @classmethod
    def open_form(cls, order_id):
        with testit.step(f'Открыть форму редактирования ПИР/СМР по заявке: {order_id}'):
            cls.open_with_path(f'{cls.path}{order_id}')

    @classmethod
    def click_show_all_works(cls):
        with testit.step(f'Нажать на кнопку "Отобразить все работы"'):
            Locator(cls._LOCATOR_BTN_SHOW_ALL_WORKS).click()

    @classmethod
    def get_all_works(cls) -> list[Locator]:
        with testit.step('Получить все работы'):
            return Locator(cls._LOCATOR_INPUTS_VALUE_ALL_WORKS).all

    @classmethod
    def cnt_visible_works(cls) -> int:
        cnt_works = Locator(cls._LOCATOR_INPUTS_VALUE_ALL_WORKS).count
        with testit.step(f'Посчитать количество отображаемых работы: {cnt_works}'):
            return cnt_works

    @classmethod
    def set_random_value_for_works(cls):

        works = cls.get_all_works()

        for _ in range(3):
            random_value = int(random.randrange(1, 10))

            random_work_position = random.randrange(0, stop=cls.cnt_visible_works())
            code_work = works[random_work_position].get_attribute('title')

            with testit.step(f'Установить работу по id {code_work} со значением {random_value}'):
                works[random_work_position].locator('//input').fill(str(random_value))

    @classmethod
    def delete_all_works(cls):
        works = cls.cnt_visible_works()

        for work in range(works):
            Locator(cls._LOCATOR_BTN_DELETE_WORKS).click()

    @classmethod
    def save_works(cls):
        with testit.step(f'Нажать на кнопку "Сохранить"'):
            Locator(cls._LOCATOR_BTN_SAVE_WORKS).click()

    @classmethod
    def check_save_changes(cls):
        with testit.step(f'Проверить отрбражение информации о сохранении работ'):
            if Locator(cls._LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED).is_on_page():
                return True
            else:
                raise Exception('Работы не изменены')

    @classmethod
    @testit.step('Добавить рандомные работы и сохранить')
    def fill_and_save_random_works(cls):
        cls.click_show_all_works()
        cls.set_random_value_for_works()
        cls.save_works()
        cls.check_save_changes()
