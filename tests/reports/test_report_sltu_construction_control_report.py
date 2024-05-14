import pytest
import testit

from page_objects.reports.SLTUConstructionControlReport import SLTUConstructionControlReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по контролю занесения данных в СЛТУ"')
@testit.description('Проверяется открытие отчёта "Отчёт по контролю занесения данных в СЛТУ"')
@pytest.mark.smoke
def test_open_report_sltu_construction_control_report(driver):
    SLTUConstructionControlReport(driver).open()
    assert SLTUConstructionControlReport(driver).check_report()
