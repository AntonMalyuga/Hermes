import pytest
import testit
from page_objects.reports.B2CConstructionReport import B2CConstructionReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный отчёт по строительству B2C"')
@testit.description('Проверить открытие отчёта "Детальный отчёт по строительству B2C"')
@pytest.mark.smoke
def test_open_report_b2c_construction_report(driver):
    B2CConstructionReport(driver).open()
    assert B2CConstructionReport(driver).check_report()
