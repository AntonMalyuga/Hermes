import time
import testit
from page import Page
from locator import Locator, Select, Input


class ComponentCapitalCosts(Page):
    name = 'B2C: Прочие капитальные затраты'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]'
    _LOCATOR_FORM_OTHER_CAPITAL_COSTS = f'//div[@class="expenses-monitoring"]//span[contains(., "Прочие капитальные расходы")]'
    _LOCATOR_FORM_OPEN_EDITOR_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Редактировать прочие капитальные расходы")]]'
    _LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Добавить строку")]]'
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE = f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "name")]]'
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL = f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "cost")]]'
    _LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON = f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Сохранить прочие капитальные расходы")]]'

    @classmethod
    def open_drop_down_panel(cls):
        with testit.step(f'Открыть выпадающую панель', 'Панель открыта'):
            Locator(cls._LOCATOR_FORM_OTHER_CAPITAL_COSTS).click()

    @classmethod
    def open_editor(cls):
        with testit.step(f'Открыть редактор', 'Редактор открыт'):
            Locator(cls._LOCATOR_FORM_OPEN_EDITOR_BUTTON).click()

    @classmethod
    def push_add_other_capital_costs_button(cls):
        with testit.step(f'Нажать кнопку "другие капитальные расходы"', 'Кнопка нажата'):
            Locator(cls._LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON).click()

    @classmethod
    def fill_other_capital_costs_out_rate_form(cls, name: str):
        with testit.step(f'Заполнить имя в форме других расходов "{name}"'):
            Input(cls._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE).input(f'{name} {time.time()}')

    @classmethod
    def fill_other_capital_costs_out_rate_total(cls, total: int):
        with testit.step(f'Заполнить сумму в форме других расходов "{total}"'):
            Input(cls._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL).input(str(total))

    @classmethod
    def push_other_capital_costs_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения', 'Кнопка нажата'):
            Locator(cls._LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON).click()

    @classmethod
    def add_cost(cls, name: str, total: int):
        with testit.step(f'Заполнить расходы: сумму "{total}" и имя "{name}"'):
            cls.open_drop_down_panel()
            cls.open_editor()
            cls.push_add_other_capital_costs_button()
            cls.fill_other_capital_costs_out_rate_form(name)
            cls.fill_other_capital_costs_out_rate_total(total)
            cls.push_other_capital_costs_submit_button()
