import pytest

from page_objects.reports.NonSynchronizedPricesReport import NonSynchronizedPricesReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по не синхронизированным расценкам"')
@testit.description('Проверяется открытие отчёта "Отчёт по не синхронизированным расценкам"')
@pytest.mark.smoke
def test_open_report_b2c_agg_construction_report_rf(driver):
    NonSynchronizedPricesReport(driver).open()
    assert NonSynchronizedPricesReport(driver).check_report()
