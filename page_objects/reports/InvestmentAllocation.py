from ..BasePage import BasePage
import testit


class InvestmentAllocation(BasePage):
    path = 'report/investment_allocation'

    _CHECK_REPORT = 'button[formaction="/report/investment_allocation/html"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
