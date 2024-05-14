import pytest
import testit

from page_objects.reports.SLAReportByStages import SLAReportByStages


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт о результатах работы по SLA по этапам"')
@testit.description('Проверяется открытие отчёта "Отчёт о результатах работы по SLA по этапам"')
@pytest.mark.smoke
def test_open_report_sla_report_by_stages(driver):
    SLAReportByStages(driver).open()
    assert SLAReportByStages(driver).check_report()
