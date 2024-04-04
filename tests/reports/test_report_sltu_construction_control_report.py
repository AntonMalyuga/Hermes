
from page_objects.reports.SLTUConstructionControlReport import SLTUConstructionControlReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_sltu_construction_control_report(driver):
    SLTUConstructionControlReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLTUConstructionControlReport(driver).check_report()
