import pytest
import testit

from page_objects.reports.SLTUProcessingDetailedReport import SLTUProcessingDetailedReport


class TestSLTUProcessingDetailedReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUProcessingDetailedReport.open_by_default()
        assert SLTUProcessingDetailedReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUProcessingDetailedReport.open_by_default()
        assert SLTUProcessingDetailedReport.get_name_report() == SLTUProcessingDetailedReport.name
