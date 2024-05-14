from page_objects.reports.InvestmentAllocation import InvestmentAllocation
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт о результатах работы по выделению инвестиций"')
@testit.description('Проверяется открытие отчёта "Отчёт о результатах работы по выделению инвестиций"')
def test_open_report_investment_allocation(driver):
    InvestmentAllocation(driver).open()
    assert InvestmentAllocation(driver).check_report()
