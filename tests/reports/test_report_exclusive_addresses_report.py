from page_objects.reports.ExclusiveAddressesReport import ExclusiveAddressesReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по эксклюзивным адресам"')
@testit.description('Проверяется открытие отчёта "Отчёт по эксклюзивным адресам"')
def test_open_report_investment_allocation_concatenated_details(driver):
    ExclusiveAddressesReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert ExclusiveAddressesReport(driver).check_report()
