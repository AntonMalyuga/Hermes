
from page_objects.reports.SLTUControlDetExpandedReport import SLTUControlDetExpandedReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltucontrol_det_expanded_report(driver):
    SLTUControlDetExpandedReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUControlDetExpandedReport(driver).check_report()