from ..BasePage import BasePage
import allure


class SLAConcatenatedDetailsReport(BasePage):
    path = 'report/sla_concatenated_details_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_concatenated_details_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True