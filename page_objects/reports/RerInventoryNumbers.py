from ..BasePage import BasePage

class RerInventoryNumbers(BasePage):
    path = 'report/rer_inventory_numbers'

    _CHECK_REPORT = 'button[formaction="/report/rer_inventory_numbers/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True