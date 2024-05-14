import pytest
import testit

from page_objects.reports.SLAReport import SLAReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт о результатах работы по SLA"')
@testit.description('Проверяется открытие отчёта "Отчёт о результатах работы по SLA"')
@pytest.mark.smoke
def test_open_report_sla_report(driver):
    SLAReport(driver).open()
    assert SLAReport(driver).check_report()
