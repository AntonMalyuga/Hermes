from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class SLTUControlAggrReport(BasePage):
    name = 'Агрегированный Отчёт по контролю корректности данных в СЛТУ'
    path = 'report/sltucontrol_aggr_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/sltucontrol_aggr_report/html"]')
    _LOCATOR_H2_NAME_REPORT = (By.XPATH, '//h2')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True

    def get_name_report(self) -> str:
        name = self.find_element(self._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
