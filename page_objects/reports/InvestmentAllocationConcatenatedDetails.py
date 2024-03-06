from ..BasePage import BasePage

class InvestmentAllocationConcatenatedDetails(BasePage):
    path = 'report/investment_allocation_concatenated_details'

    _CHECK_REPORT = 'button[formaction="/report/investment_allocation_concatenated_details/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True