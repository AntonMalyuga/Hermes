from ..BasePage import BasePage
import allure


class KS2ByWorkflow(BasePage):
    path = 'report/ks2_by_workflow'

    _CHECK_REPORT = 'button[formaction="/report/ks2_by_workflow/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True