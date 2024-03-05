from ..BasePage import BasePage
import allure


class ContractorClientOrderReport(BasePage):
    path = 'report/contractor_client_order_report'
    _CHECK_REPORT = 'button[formaction="/report/contractor_client_order_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True