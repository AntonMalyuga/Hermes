from ..BasePage import BasePage

class SLTUConstructionControlReport(BasePage):
    path = 'report/sltu_construction_control_report'

    _CHECK_REPORT = 'button[formaction="/report/sltu_construction_control_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True