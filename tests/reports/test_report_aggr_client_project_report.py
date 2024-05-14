import pytest

from page_objects.reports.AggrClientProjectReport import AggrClientProjectReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Агрегированная Аналитика проекта"')
@testit.description('Проверяется открытие отчёта "Агрегированная Аналитика проекта"')
@pytest.mark.smoke
def test_open_report_aggr_client_project_report(driver):
    AggrClientProjectReport(driver).open()
    assert AggrClientProjectReport(driver).check_report()
