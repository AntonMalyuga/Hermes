from page_objects.reports.NewPostmonReport import NewPostmonReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_new_postmon_report(driver):
    NewPostmonReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert NewPostmonReport(driver).check_report()
