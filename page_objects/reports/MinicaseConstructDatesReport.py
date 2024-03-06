from ..BasePage import BasePage

class MinicaseConstructDatesReport(BasePage):
    path = 'report/minicase_constructdates_report'

    _CHECK_REPORT = 'button[formaction="/report/minicase_constructdates_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
