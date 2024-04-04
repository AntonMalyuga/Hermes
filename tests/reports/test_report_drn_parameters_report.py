from page_objects.reports.DrnParametersReport import DrnParametersReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_drn_parameters_report(driver):
    DrnParametersReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert DrnParametersReport(driver).check_report()