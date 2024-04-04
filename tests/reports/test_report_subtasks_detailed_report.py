
from page_objects.reports.SubtasksDetailedReport import SubtasksDetailedReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltucontrol_det_expanded_report(driver):
    SubtasksDetailedReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SubtasksDetailedReport(driver).check_report()