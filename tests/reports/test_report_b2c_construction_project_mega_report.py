from page_objects.reports.B2CConstructionProjectMegaReport import B2CConstructionProjectMegaReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_construction_project_mega_report(driver):
    B2CConstructionProjectMegaReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CConstructionProjectMegaReport(driver).check_report()
