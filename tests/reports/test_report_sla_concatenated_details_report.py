from page_objects.reports.SLAConcatenatedDetailsReport import SLAConcatenatedDetailsReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_rer_subtask(driver):
    SLAConcatenatedDetailsReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLAConcatenatedDetailsReport(driver).check_report()
