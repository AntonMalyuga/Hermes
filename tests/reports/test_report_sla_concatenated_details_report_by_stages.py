import pytest
import testit

from page_objects.reports.SLAConcatenatedDetailsReportByStages import SLAConcatenatedDetailsReportByStages


class TestSLAConcatenatedDetailsReportByStages:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAConcatenatedDetailsReportByStages.open_by_default()
        assert SLAConcatenatedDetailsReportByStages.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAConcatenatedDetailsReportByStages.open_by_default()
        assert SLAConcatenatedDetailsReportByStages.get_name_report() == SLAConcatenatedDetailsReportByStages.name
