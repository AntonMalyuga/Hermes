import pytest

from page_objects.reports.DeadlinesHistoryReport import DeadlinesHistoryReport
import testit


class TestDeadlinesHistoryReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        DeadlinesHistoryReport.open_by_default()
        assert DeadlinesHistoryReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        DeadlinesHistoryReport.open_by_default()
        assert DeadlinesHistoryReport.get_name_report() == DeadlinesHistoryReport.name
