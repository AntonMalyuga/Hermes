import pytest

from page_objects.reports.DeadlinesHistoryReport import DeadlinesHistoryReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по переносу дат и сроков"')
@testit.description('Проверяется открытие отчёта "Отчёт по переносу дат и сроков"')
@pytest.mark.smoke
def test_open_report_deadlines_history_report(driver):
    DeadlinesHistoryReport(driver).open()
    assert DeadlinesHistoryReport(driver).check_report()
