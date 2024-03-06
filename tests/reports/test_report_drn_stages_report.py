from page_objects.reports.DrnStagesReport import DrnStagesReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_drn_stages_report(driver):
    DrnStagesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert DrnStagesReport(driver).check_report()