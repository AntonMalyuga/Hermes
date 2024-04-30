from page_objects.reports.InvestmentAllocationConcatenatedDetails import InvestmentAllocationConcatenatedDetails
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName(
    'Проверить открытие отчёта "Соединенный детальный отчёт о результатах работы по выделению инвестиций"')
@testit.description(
    'Проверяется открытие отчёта "Соединенный детальный отчёт о результатах работы по выделению инвестиций"')
def test_open_report_investment_allocation_concatenated_details(driver):
    InvestmentAllocationConcatenatedDetails(driver).open()
    UserLoginForm(driver).authorization_default()
    assert InvestmentAllocationConcatenatedDetails(driver).check_report()
