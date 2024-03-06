from ..BasePage import BasePage

class LocalNormocontrolMega(BasePage):
    path = 'report/localnormocontrolmega'
    _CHECK_REPORT = 'button[formaction="/report/localnormocontrolmega/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
