import testit
import pytest
from page_objects.reports.SLADynamicReport import SLADynamicReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Динамика показателей по SLA"')
@testit.description('Проверяется открытие отчёта "Динамика показателей по SLA"')
def test_open_report_sla_dynamic_report(driver):
    SLADynamicReport(driver).open()
    assert SLADynamicReport(driver).check_report()


@testit.title('reports')
@testit.displayName('Проверить наименование отчёта "Динамика показателей по SLA"')
@testit.description('Проверяется наименование отчёта "Динамика показателей по SLA"')
@pytest.mark.smoke
def test_check_name_sla_dynamic_report(driver):
    SLADynamicReport(driver).open()
    assert SLADynamicReport(driver).get_name_report() == SLADynamicReport(driver).name
