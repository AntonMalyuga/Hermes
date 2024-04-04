from page_objects.reports.SLTUControlAggrReport import SLTUControlAggrReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltucontrol_aggr_report(driver):
    SLTUControlAggrReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLTUControlAggrReport(driver).check_report()
