from page_objects.reports.LocalNormocontrolMega import LocalNormocontrolMega
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Нормоконтроль (формируемый)"')
@testit.description('Проверяется открытие отчёта "Нормоконтроль (формируемый)"')
def test_open_report_local_normocontrol_mega(driver):
    LocalNormocontrolMega(driver).open()
    UserLoginForm(driver).authorization_default()
    assert LocalNormocontrolMega(driver).check_report()
