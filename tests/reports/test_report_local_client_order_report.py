import pytest

from page_objects.reports.LocalClientOrderReport import LocalClientOrderReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по клиентским заявкам (формируемый)"')
@testit.description('Проверяется открытие отчёта "Отчёт по клиентским заявкам (формируемый)"')
@pytest.mark.smoke
def test_open_report_local_client_order_report(driver):
    LocalClientOrderReport(driver).open()
    assert LocalClientOrderReport(driver).check_report()
