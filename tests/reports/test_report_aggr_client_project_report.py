from page_objects.reports.AggrClientProjectReport import AggrClientProjectReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_aggr_client_project_report(driver):
    AggrClientProjectReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert AggrClientProjectReport(driver).check_report()
