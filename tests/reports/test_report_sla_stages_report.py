import pytest
import testit

from page_objects.reports.SLAStagesReport import SLAStagesReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Анализ просроченных клиентских заявок"')
@testit.description('Проверяется открытие отчёта "Анализ просроченных клиентских заявок"')
@pytest.mark.smoke
def test_open_report_sla_stages_report(driver):
    SLAStagesReport(driver).open()
    assert SLAStagesReport(driver).check_report()
