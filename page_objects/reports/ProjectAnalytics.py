from ..BasePage import BasePage

class ProjectAnalytics(BasePage):
    path = 'report/projectanalytics'
    _CHECK_REPORT = 'button[formaction="/report/projectanalytics/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
