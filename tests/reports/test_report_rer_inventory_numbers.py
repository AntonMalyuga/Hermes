import pytest

from page_objects.reports.RerInventoryNumbers import RerInventoryNumbers
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчет по инвентарным номерам"')
@testit.description('Проверяется открытие отчёта "Отчет по инвентарным номерам"')
@pytest.mark.smoke
def test_open_report_rer_inventory_numbers(driver):
    RerInventoryNumbers(driver).open()
    assert RerInventoryNumbers(driver).check_report()
