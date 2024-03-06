from ..BasePage import BasePage

class DrnParametersReport(BasePage):
    path = 'report/drn_parameters_report'
    _CHECK_REPORT = 'button[formaction="/report/drn_parameters_report/html"'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True