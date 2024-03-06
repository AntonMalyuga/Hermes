from page_objects.reports.SLAReportByStages import SLAReportByStages
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_sla_report_by_stages(driver):
    SLAReportByStages(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAReportByStages(driver).check_report()
