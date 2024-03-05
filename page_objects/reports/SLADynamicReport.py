from ..BasePage import BasePage
import allure


class SLADynamicReport(BasePage):
    path = 'report/sla_dynamic_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_dynamic_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True