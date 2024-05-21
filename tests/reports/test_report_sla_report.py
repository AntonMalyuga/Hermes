import pytest
import testit

from page_objects.reports.SLAReport import SLAReport


class TestSLAReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAReport.open_by_default()
        assert SLAReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAReport.open_by_default()
        assert SLAReport.get_name_report() == SLAReport.name
