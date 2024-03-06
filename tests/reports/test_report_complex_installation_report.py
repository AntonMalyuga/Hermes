from page_objects.reports.ComplexInstallationReport import ComplexInstallationReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_complex_installation_report(driver):
    ComplexInstallationReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert ComplexInstallationReport(driver).check_report()
