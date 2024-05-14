from page_objects.reports.O2OMegaReport import O2OMegaReport
import pytest
import testit



@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт БП O2O"')
@testit.description('Проверяется открытие отчёта "Отчёт БП O2O"')
@pytest.mark.skip('Отчёт удалён HE-13415')
def test_open_report_o2o_mega_report(driver):
    O2OMegaReport(driver).open()
    assert O2OMegaReport(driver).check_report()
