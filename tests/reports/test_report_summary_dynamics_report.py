
from page_objects.reports.SummaryDynamicsReport import SummaryDynamicsReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_summary_dynamics_report(driver):
    SummaryDynamicsReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SummaryDynamicsReport(driver).check_report()
