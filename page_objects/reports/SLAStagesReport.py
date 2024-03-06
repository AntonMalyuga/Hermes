from ..BasePage import BasePage

class SLAStagesReport(BasePage):
    path = 'report/sla_stages_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_stages_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True