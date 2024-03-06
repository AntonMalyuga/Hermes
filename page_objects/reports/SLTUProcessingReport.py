from ..BasePage import BasePage

class SLTUProcessingReport(BasePage):
    path = 'report/sltu_processing_report'

    _CHECK_REPORT = 'button[formaction="/report/sltu_processing_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
