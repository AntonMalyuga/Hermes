import testit

from page_objects.reports.SLAContractorRatingReport import SLAContractorRatingReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт рейтинг Подрядчиков по SLA"')
@testit.description('Проверяется открытие отчёта "Отчёт рейтинг Подрядчиков по SLA"')
def test_open_report_sla_contractor_rating_report(driver):
    SLAContractorRatingReport(driver).open()
    assert SLAContractorRatingReport(driver).check_report()