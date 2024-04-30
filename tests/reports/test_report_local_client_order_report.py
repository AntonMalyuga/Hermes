from page_objects.reports.LocalClientOrderReport import LocalClientOrderReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по клиентским заявкам (формируемый)"')
@testit.description('Проверяется открытие отчёта "Отчёт по клиентским заявкам (формируемый)"')
def test_open_report_local_client_order_report(driver):
    LocalClientOrderReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert LocalClientOrderReport(driver).check_report()
