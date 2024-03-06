from page_objects.reports.SLTUProcessingReport import SLTUProcessingReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltu_processing_report(driver):
    SLTUProcessingReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUProcessingReport(driver).check_report()
