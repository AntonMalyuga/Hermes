
from ..BasePage import BasePage

class MinicaseB2BServiceReport(BasePage):
    path = 'report/minicase_b2b_service_report'
    _CHECK_REPORT = 'button[formaction="/report/minicase_b2b_service_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True




