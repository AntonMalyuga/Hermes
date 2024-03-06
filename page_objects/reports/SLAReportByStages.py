from ..BasePage import BasePage

class SLAReportByStages(BasePage):
    path = 'report/sla_report_by_stages'

    _CHECK_REPORT = 'button[formaction="/report/sla_report_by_stages/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True