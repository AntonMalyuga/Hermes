from page_objects.reports.B2CConstructionReport import B2CConstructionReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный отчёт по строительству B2C"')
@testit.description('Проверить открытие отчёта "Детальный отчёт по строительству B2C"')
def test_open_report_b2c_construction_report(driver):
    B2CConstructionReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert B2CConstructionReport(driver).check_report()
