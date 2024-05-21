import pytest
import testit

from page_objects.reports.SummaryDynamicsReport import SummaryDynamicsReport


class TestSummaryDynamicsReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SummaryDynamicsReport.open_by_default()
        assert SummaryDynamicsReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SummaryDynamicsReport.open_by_default()
        assert SummaryDynamicsReport.get_name_report() == SummaryDynamicsReport.name
