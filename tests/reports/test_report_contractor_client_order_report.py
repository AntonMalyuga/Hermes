from page_objects.reports.ContractorClientOrderReport import ContractorClientOrderReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по КЗ для Подрядчиков"')
@testit.description('Проверяется открытие отчёта "Отчёт по КЗ для Подрядчиков"')
def test_open_report_contractor_client_order_report(driver):
    ContractorClientOrderReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert ContractorClientOrderReport(driver).check_report()
