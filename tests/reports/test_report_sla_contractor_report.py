import testit

from page_objects.reports.SLAContractorReport import SLAContractorReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по Подрядчикам"')
@testit.description('Проверяется открытие отчёта "Отчёт по Подрядчикам"')
def test_open_report_sla_contractor_report(driver):
    SLAContractorReport(driver).open()
    assert SLAContractorReport(driver).check_report()
