import pytest

from page_objects.reports.ExclusiveAddressesReport import ExclusiveAddressesReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по эксклюзивным адресам"')
@testit.description('Проверяется открытие отчёта "Отчёт по эксклюзивным адресам"')
@pytest.mark.smoke
def test_open_report_investment_allocation_concatenated_details(driver):
    ExclusiveAddressesReport(driver).open()
    assert ExclusiveAddressesReport(driver).check_report()
