from page_objects.reports.EmployeeReport import EmployeeReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_employee_report(driver):
    EmployeeReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert EmployeeReport(driver).check_report()