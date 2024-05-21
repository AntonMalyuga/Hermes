import pytest
import testit

from page_objects.reports.SLTUProcessingReport import SLTUProcessingReport


class TestSLTUProcessingReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUProcessingReport.open_by_default()
        assert SLTUProcessingReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUProcessingReport.open_by_default()
        assert SLTUProcessingReport.get_name_report() == SLTUProcessingReport.name
