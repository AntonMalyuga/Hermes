from ..BasePage import BasePage
import allure


class SLTUErrorsReport(BasePage):
    path = 'report/sltu_errors_report'

    _CHECK_REPORT = 'button[formaction="/report/sltu_errors_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True