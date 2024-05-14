from page_objects.reports.B2CAggConstructionReportRF import B2CAggConstructionReportRF
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Сводный отчёт по строительству B2C"')
@testit.description('Проверяется открытие отчёта "Сводный отчёт по строительству B2C"')
def test_open_report_b2c_agg_construction_report_rf(driver):
    B2CAggConstructionReportRF(driver).open()
    assert B2CAggConstructionReportRF(driver).check_report()
