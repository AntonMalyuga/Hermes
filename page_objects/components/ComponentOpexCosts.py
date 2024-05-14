import time
import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order


class ComponentOpexCosts(Order):

    name = 'B2C: Прочие операционные расходы'

    _LOCATOR_FORM_OTHER_CAPITAL_COSTS = (
        By.XPATH, f'//div[@class="expenses-monitoring"]//span[contains(., "Прочие операционные расходы")]')
    _LOCATOR_FORM_OPEN_EDITOR_BUTTON = (By.XPATH,
                                        f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Редактировать прочие операционные расходы")]]')
    _LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON = (
        By.XPATH, f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Добавить строку")]]')
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE = (By.XPATH,
                                                  f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "name")]]')
    _LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL = (By.XPATH,
                                                   f'//div[@class="expenses-monitoring"]//table[@class[contains(.,"b2c-other-capexes-table")]]//tr[@data-order][last()]//input[@name[contains(., "cost")]]')
    _LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON = (By.XPATH,
                                                       f'//div[@class="expenses-monitoring"]//button[@title[contains(., "Сохранить прочие капитальные расходы")]]')

    def open_drop_down_panel(self):
        with testit.step(f'Открыть выпадающую панель'):
            self.find_element(locator=self._LOCATOR_FORM_OTHER_CAPITAL_COSTS).click()

    def open_editor(self):
        with testit.step(f'Открыть редактор'):
            self.find_element(locator=self._LOCATOR_FORM_OPEN_EDITOR_BUTTON).click()

    def push_add_other_opex_costs_button(self):
        with testit.step(f'Нажать кнопку редактирования расходов OPEX'):
            self.find_element(locator=self._LOCATOR_PUSH_FORM_ADD_OTHER_CAPITAL_COSTS_BUTTON).click()

    def fill_other_opex_costs_out_rate_form(self, name: str):
        with testit.step(f'Заполнить форму дополнительных расходов OPEX "{name}"'):
            self.find_element(locator=self._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_RATE).send_keys(
                f'{name} {time.time()}')

    def fill_other_opex_costs_out_rate_total(self, total: int):
        with testit.step(f'Заполнить форму суммарных дополнительных расходов OPEX "{total}"'):
            self.find_element(locator=self._LOCATOR_FORM_ADD_OTHER_CAPITAL_COSTS_TOTAL).send_keys(total)

    def push_other_opex_costs_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения'):
            self.find_element(locator=self._LOCATOR_PUSH_SUBMIT_OTHER_CAPITAL_COSTS_BUTTON).click()

    def add_cost(self, name: str, total: int):
        with testit.step(f'Заполнить расходы OPEX: статья расходов "{name}" и суммарные расходы "{total}"'):
            self.open_drop_down_panel()
            self.open_editor()
            self.push_add_other_opex_costs_button()
            self.fill_other_opex_costs_out_rate_form(name)
            self.fill_other_opex_costs_out_rate_total(total)
            self.push_other_opex_costs_submit_button()
