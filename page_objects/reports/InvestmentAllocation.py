from ..BasePage import BasePage

class InvestmentAllocation(BasePage):
    path = 'report/investment_allocation'

    _CHECK_REPORT = 'button[formaction="/report/investment_allocation/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True