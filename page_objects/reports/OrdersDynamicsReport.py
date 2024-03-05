

from ..BasePage import BasePage
import allure


class OrdersDynamicsReport(BasePage):
    path = 'report/orders_dynamics_report'
    _CHECK_REPORT = 'button[formaction="/report/orders_dynamics_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True