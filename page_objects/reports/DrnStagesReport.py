from ..BasePage import BasePage

class DrnStagesReport(BasePage):
    path = 'report/drn_stages_report'

    _CHECK_REPORT = 'button[formaction="/report/drn_stages_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True