import pytest

from page_objects.reports.KS2ByWorkflow import KS2ByWorkflow
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по КС-2"')
@testit.description('Проверяется открытие отчёта "Отчёт по КС-2"')
@pytest.mark.smoke
def test_open_report_minicase_construct_dates_report(driver):
    KS2ByWorkflow(driver).open()
    assert KS2ByWorkflow(driver).check_report()
