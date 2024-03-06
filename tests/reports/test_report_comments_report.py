from page_objects.reports.CommentsReport import CommentsReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_complex_installation_report(driver):
    CommentsReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert CommentsReport(driver).check_report()
