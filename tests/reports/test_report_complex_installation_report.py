from page_objects.reports.ComplexInstallationReport import ComplexInstallationReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по заявкам со Сложной инсталляцией"')
@testit.description('Проверяется открытие отчёта "Отчёт по заявкам со Сложной инсталляцией"')
def test_open_report_complex_installation_report(driver):
    ComplexInstallationReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert ComplexInstallationReport(driver).check_report()
