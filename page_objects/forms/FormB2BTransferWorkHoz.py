from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import testit


class FormB2BTransferWorkHoz:
    name = 'B2B: Выбор работ хоз. способом'
    path = 'aggregator/works/'

    _LOCATOR_CHECKBOX_TRANSFER_HOZ = (
        By.XPATH, '//form[contains(@action,"works")]//input[@type="checkbox"]//following::label[1]')
    _LOCATOR_BTN_SAVE = '//form[contains(@action,"works")]//button[@type="submit"]')
    _LOCATOR_DIV_CHECK_CHANGES = '//div[@class="alert alert-success alert-dismissable"]')

    def open_form(self, order_id: int):
        with testit.step(f'Открыть экранную форму по заявке {order_id}'):
            self.open_for_link(f'{self.path}{order_id}')

    def get_all_switch_hoz(self) -> list[WebElement]:
        with testit.step('Получить все работы'):
            return self.find_elements(self._LOCATOR_CHECKBOX_TRANSFER_HOZ)

    def save(self):
        with testit.step('Нажать на кнопку сохранения работ'):
            self.find_element(self._LOCATOR_BTN_SAVE).click()

    def check_save_changes(self) -> bool:
        with testit.step('Проверка успешного переноса работ', 'Работы успешно перенесены'):
            if self.find_element(self._LOCATOR_DIV_CHECK_CHANGES).is_enabled():
                return True
            else:
                raise Exception('Работы не перенесены')

    @testit.step('Включение всех работ')
    def set_all_works_hoz(self):
        for switch in self.get_all_switch_hoz():
            switch.click()
        self.save()
        self.check_save_changes()
        self.close()
