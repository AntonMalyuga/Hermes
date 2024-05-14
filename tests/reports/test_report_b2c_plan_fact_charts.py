import pytest

from page_objects.reports.B2CPlanFactCharts import B2CPlanFactCharts
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Графические отчёты План/Факт"')
@testit.description('Проверить открытие отчёта "Графические отчёты План/Факт"')
@pytest.mark.smoke
def test_open_report_b2c_plan_fact_charts(driver):
    B2CPlanFactCharts(driver).open()
    assert B2CPlanFactCharts(driver).check_report()
