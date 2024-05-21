import pytest
import testit

from page_objects.reports.SLAReportByStages import SLAReportByStages


class TestSLAReportByStages:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAReportByStages.open_by_default()
        assert SLAReportByStages.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAReportByStages.open_by_default()
        assert SLAReportByStages.get_name_report() == SLAReportByStages.name
