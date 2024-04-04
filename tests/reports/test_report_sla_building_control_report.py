from page_objects.reports.SLABuildingControlReport import SLABuildingControlReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_sla_building_control_report(driver):
    SLABuildingControlReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLABuildingControlReport(driver).check_report()