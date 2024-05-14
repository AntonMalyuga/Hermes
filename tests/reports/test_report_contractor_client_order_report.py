import pytest

from page_objects.reports.ContractorClientOrderReport import ContractorClientOrderReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по КЗ для Подрядчиков"')
@testit.description('Проверяется открытие отчёта "Отчёт по КЗ для Подрядчиков"')
@pytest.mark.smoke
def test_open_report_contractor_client_order_report(driver):
    ContractorClientOrderReport(driver).open()
    assert ContractorClientOrderReport(driver).check_report()
