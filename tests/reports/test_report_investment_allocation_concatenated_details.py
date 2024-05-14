import pytest

from page_objects.reports.InvestmentAllocationConcatenatedDetails import InvestmentAllocationConcatenatedDetails
import testit


@testit.title('reports')
@testit.displayName(
    'Проверить открытие отчёта "Соединенный детальный отчёт о результатах работы по выделению инвестиций"')
@testit.description(
    'Проверяется открытие отчёта "Соединенный детальный отчёт о результатах работы по выделению инвестиций"')
@pytest.mark.smoke
def test_open_report_investment_allocation_concatenated_details(driver):
    InvestmentAllocationConcatenatedDetails(driver).open()
    assert InvestmentAllocationConcatenatedDetails(driver).check_report()
