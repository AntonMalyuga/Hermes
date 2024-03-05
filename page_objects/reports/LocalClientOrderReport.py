from ..BasePage import BasePage
import allure


class LocalClientOrderReport(BasePage):
    path = 'report/local_client_order_report'
    _CHECK_REPORT = 'button[formaction="/report/local_client_order_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
