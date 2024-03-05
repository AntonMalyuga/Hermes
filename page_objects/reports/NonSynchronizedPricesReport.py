from ..BasePage import BasePage
import allure


class NonSynchronizedPricesReport(BasePage):
    path = 'report/non_synchronized_prices_report'

    _CHECK_REPORT = 'button[formaction="/report/non_synchronized_prices_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True