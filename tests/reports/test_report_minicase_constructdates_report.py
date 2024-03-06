from page_objects.reports.MinicaseConstructDatesReport import MinicaseConstructDatesReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_minicase_construct_dates_report(driver):
    MinicaseConstructDatesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert MinicaseConstructDatesReport(driver).check_report()
