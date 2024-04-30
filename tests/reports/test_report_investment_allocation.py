from page_objects.reports.InvestmentAllocation import InvestmentAllocation
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт о результатах работы по выделению инвестиций"')
@testit.description('Проверяется открытие отчёта "Отчёт о результатах работы по выделению инвестиций"')
def test_open_report_investment_allocation(driver):
    InvestmentAllocation(driver).open()
    UserLoginForm(driver).authorization_default()
    assert InvestmentAllocation(driver).check_report()
