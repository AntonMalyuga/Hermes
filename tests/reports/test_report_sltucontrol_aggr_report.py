import testit

from page_objects.reports.SLTUControlAggrReport import SLTUControlAggrReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Агрегированный Отчёт по контролю корректности данных в СЛТУ"')
@testit.description('Проверяется открытие отчёта "Агрегированный Отчёт по контролю корректности данных в СЛТУ"')
def test_open_report_sltucontrol_aggr_report(driver):
    SLTUControlAggrReport(driver).open()
    assert SLTUControlAggrReport(driver).check_report()
