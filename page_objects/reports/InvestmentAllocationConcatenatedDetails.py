from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class InvestmentAllocationConcatenatedDetails(BasePage):
    name = 'Соединенный детальный отчёт о результатах работы по выделению инвестиций'
    path = 'report/investment_allocation_concatenated_details'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/investment_allocation_concatenated_details/html"]')
    _LOCATOR_H2_NAME_REPORT = (By.XPATH, '//h2')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True

    def get_name_report(self) -> str:
        name = self.find_element(self._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
