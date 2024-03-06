from page_objects.reports.SLAConcatenatedDetailsReportByStages import SLAConcatenatedDetailsReportByStages
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_sla_concatenated_details_report_by_stages(driver):
    SLAConcatenatedDetailsReportByStages(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAConcatenatedDetailsReportByStages(driver).check_report()
