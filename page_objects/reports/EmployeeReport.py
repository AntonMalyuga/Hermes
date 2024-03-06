from ..BasePage import BasePage

class EmployeeReport(BasePage):
    path = 'report/employee_report'

    _CHECK_REPORT = 'button[formaction="/report/employee_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True