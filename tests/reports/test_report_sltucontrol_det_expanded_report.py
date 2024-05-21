import pytest
import testit

from page_objects.reports.SLTUControlDetExpandedReport import SLTUControlDetExpandedReport


class TestSLTUControlDetExpandedReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUControlDetExpandedReport.open_by_default()
        assert SLTUControlDetExpandedReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUControlDetExpandedReport.open_by_default()
        assert SLTUControlDetExpandedReport.get_name_report() == SLTUControlDetExpandedReport.name
