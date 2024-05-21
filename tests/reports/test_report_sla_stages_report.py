import pytest
import testit

from page_objects.reports.SLAStagesReport import SLAStagesReport


class TestSLAStagesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAStagesReport.open_by_default()
        assert SLAStagesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAStagesReport.open_by_default()
        assert SLAStagesReport.get_name_report() == SLAStagesReport.name
