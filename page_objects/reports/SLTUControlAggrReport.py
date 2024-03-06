from ..BasePage import BasePage

class SLTUControlAggrReport(BasePage):
    path = 'report/sltucontrol_aggr_report'

    _CHECK_REPORT = 'button[formaction="/report/sltucontrol_aggr_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
