from ..BasePage import BasePage

class O2OMegaReport(BasePage):
    path = 'report/o2o_mega_report'
    _CHECK_REPORT = 'button[formaction="/report/o2o_mega_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True