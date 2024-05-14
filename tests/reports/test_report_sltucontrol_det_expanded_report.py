import pytest
import testit

from page_objects.reports.SLTUControlDetExpandedReport import SLTUControlDetExpandedReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный Отчёт по контролю корректности данных в СЛТУ (расширенный)"')
@testit.description(
    'Проверяется открытие отчёта "Детальный Отчёт по контролю корректности данных в СЛТУ (расширенный)"')
@pytest.mark.smoke
def test_open_report_sltucontrol_det_expanded_report(driver):
    SLTUControlDetExpandedReport(driver).open()
    assert SLTUControlDetExpandedReport(driver).check_report()
