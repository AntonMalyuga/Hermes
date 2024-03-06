from ..BasePage import BasePage

class B2CSmrMegaReport(BasePage):
    path = 'report/b2c_smr_mega_report'

    _CHECK_REPORT = 'button[formaction="/report/b2c_smr_mega_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True