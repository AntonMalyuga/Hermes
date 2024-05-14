import pytest
import testit

from page_objects.reports.SLTUControlDetReport import SLTUControlDetReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный Отчёт по контролю корректности данных в СЛТУ"')
@testit.description('Проверяется открытие отчёта "Детальный Отчёт по контролю корректности данных в СЛТУ"')
@pytest.mark.smoke
def test_open_report_sltucontrol_det_report(driver):
    SLTUControlDetReport(driver).open()
    assert SLTUControlDetReport(driver).check_report()
