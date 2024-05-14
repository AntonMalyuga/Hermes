from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class InvestmentAllocationConcatenatedDetails(BasePage):
    name = 'Соединенный детальный отчёт о результатах работы по выделению инвестиций'
    path = 'report/investment_allocation_concatenated_details'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/investment_allocation_concatenated_details/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
