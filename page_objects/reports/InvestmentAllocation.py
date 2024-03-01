from ..BasePage import BasePage
import allure


class InvestmentAllocation(BasePage):
    path = 'report/investment_allocation'

    _CHECK_REPORT = 'button[formaction="/report/investment_allocation/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True