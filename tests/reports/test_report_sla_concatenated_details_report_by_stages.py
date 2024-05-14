import testit

from page_objects.reports.SLAConcatenatedDetailsReportByStages import SLAConcatenatedDetailsReportByStages


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Соединенный Детальный отчёт о результатах работы по SLA по этапам"')
@testit.description('Проверяется открытие отчёта "Соединенный Детальный отчёт о результатах работы по SLA по этапам"')
def test_open_report_sla_concatenated_details_report_by_stages(driver):
    SLAConcatenatedDetailsReportByStages(driver).open()
    assert SLAConcatenatedDetailsReportByStages(driver).check_report()
