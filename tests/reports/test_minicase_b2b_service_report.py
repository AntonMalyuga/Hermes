from page_objects.reports.MinicaseB2BServiceReport import MinicaseB2BServiceReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_plan_fact_charts(driver):
    MinicaseB2BServiceReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert MinicaseB2BServiceReport(driver).check_report()
