import pytest
import testit

from page_objects.reports.SummaryDynamicsReport import SummaryDynamicsReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Сводный отчёт по динамике заявок за период"')
@testit.description('Проверяется открытие отчёта "Сводный отчёт по динамике заявок за период"')
@pytest.mark.smoke
def test_open_report_summary_dynamics_report(driver):
    SummaryDynamicsReport(driver).open()
    assert SummaryDynamicsReport(driver).check_report()
