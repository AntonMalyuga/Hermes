import testit

from page_objects.reports.SLTUErrorsReport import SLTUErrorsReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по запросам АПТВ в шину"')
@testit.description('Проверяется открытие отчёта "Отчёт по запросам АПТВ в шину"')
def test_open_report_b2c_departments_rating(driver):
    SLTUErrorsReport(driver).open()
    assert SLTUErrorsReport(driver).check_report()
