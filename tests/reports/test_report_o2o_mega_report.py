from page_objects.reports.O2OMegaReport import O2OMegaReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_o2o_mega_report(driver):
    O2OMegaReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert O2OMegaReport(driver).check_report()