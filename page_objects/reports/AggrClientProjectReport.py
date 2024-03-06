from ..BasePage import BasePage


class AggrClientProjectReport(BasePage):
    path = 'report/aggr_client_project_report'

    _CHECK_REPORT = 'button[formaction="/report/aggr_client_project_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
