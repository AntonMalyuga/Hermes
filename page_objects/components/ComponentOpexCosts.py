import time
import testit
from page import Page
from locator import Locator, Input


class ComponentOpexCosts(Page):
    name = 'B2C: Прочие операционные расходы'

    _LOCATOR_FORM_OTHER_CAPITAL_COSTS = f'//div[@class="expenses-monitoring"]//span[contains(., "Прочие операционные расходы")]'
    _LOCATOR_FORM_OPEN_EDITOR_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Редактировать прочие операционные расходы")]]'
    _LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Добавить строку")]]'
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE = f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "name")]]'
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL = f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "cost")]]'
    _LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Сохранить прочие капитальные расходы")]]'

    @classmethod
    def open_drop_down_panel(cls):
        with testit.step(f'Открыть выпадающую панель'):
            Locator(cls._LOCATOR_FORM_OTHER_CAPITAL_COSTS).click()

    @classmethod
    def open_editor(cls):
        with testit.step(f'Открыть редактор'):
            Locator(cls._LOCATOR_FORM_OPEN_EDITOR_BUTTON).click()

    @classmethod
    def push_add_other_opex_costs_button(cls):
        with testit.step(f'Нажать кнопку редактирования расходов OPEX'):
            Locator(cls._LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON).click()

    @classmethod
    def fill_other_opex_costs_out_rate_form(cls, name: str):
        with testit.step(f'Заполнить форму дополнительных расходов OPEX "{name}"'):
            Input(cls._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE).input(f'{name} {time.time()}')

    @classmethod
    def fill_other_opex_costs_out_rate_total(cls, total: int):
        with testit.step(f'Заполнить форму суммарных дополнительных расходов OPEX "{total}"'):
            Input(cls._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL).input(total)

    @classmethod
    def push_other_opex_costs_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON).click()

    @classmethod
    def add_cost(cls, name: str, total: int):
        with testit.step(f'Заполнить расходы OPEX: статья расходов "{name}" и суммарные расходы "{total}"'):
            cls.open_drop_down_panel()
            cls.open_editor()
            cls.push_add_other_opex_costs_button()
            cls.fill_other_opex_costs_out_rate_form(name)
            cls.fill_other_opex_costs_out_rate_total(total)
            cls.push_other_opex_costs_submit_button()
