import testit

from page_objects.reports.SLTUProcessingReport import SLTUProcessingReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по сквозному прохождению заявок на организацию"')
@testit.description('Проверяется открытие отчёта "Отчёт по сквозному прохождению заявок на организацию"')
def test_open_report_sltu_processing_report(driver):
    SLTUProcessingReport(driver).open()
    assert SLTUProcessingReport(driver).check_report()
