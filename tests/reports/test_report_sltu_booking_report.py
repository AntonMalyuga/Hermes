from page_objects.reports.SLTUBookingReport import SLTUBookingReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_sltu_booking_report(driver):
    SLTUBookingReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLTUBookingReport(driver).check_report()
