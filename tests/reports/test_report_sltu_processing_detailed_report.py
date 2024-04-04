from page_objects.reports.SLTUProcessingDetailedReport import SLTUProcessingDetailedReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltu_processing_detailed_report(driver):
    SLTUProcessingDetailedReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLTUProcessingDetailedReport(driver).check_report()
