
from page_objects.reports.SLTUControlDetReport import SLTUControlDetReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_sltucontrol_det_report(driver):
    SLTUControlDetReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLTUControlDetReport(driver).check_report()