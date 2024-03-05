from ..BasePage import BasePage
import allure


class SLTUControlDetReport(BasePage):
    path = 'report/sltucontrol_det_report'

    _CHECK_REPORT = 'button[formaction="/report/sltucontrol_det_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True