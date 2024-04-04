from page_objects.reports.B2CSmrMegaReport import B2CSmrMegaReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_smr_mega_report(driver):
    B2CSmrMegaReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert B2CSmrMegaReport(driver).check_report()