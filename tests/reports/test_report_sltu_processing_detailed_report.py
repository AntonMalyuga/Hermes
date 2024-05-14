import pytest
import testit

from page_objects.reports.SLTUProcessingDetailedReport import SLTUProcessingDetailedReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по сквозному прохождению заявок на организацию (детальный)"')
@testit.description('Проверяется открытие отчёта "Отчёт по сквозному прохождению заявок на организацию (детальный)"')
@pytest.mark.smoke
def test_open_report_sltu_processing_detailed_report(driver):
    SLTUProcessingDetailedReport(driver).open()
    assert SLTUProcessingDetailedReport(driver).check_report()
