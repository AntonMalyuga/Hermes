from page_objects.reports.SLAReport import SLAReport
from page_objects.elements.UserLoginForm import UserLoginForm



def test_open_report_sla_report(driver):
    SLAReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLAReport(driver).check_report()
