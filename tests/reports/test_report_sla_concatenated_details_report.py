import pytest
import testit

from page_objects.reports.SLAConcatenatedDetailsReport import SLAConcatenatedDetailsReport


class TestSLAConcatenatedDetailsReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAConcatenatedDetailsReport.open_by_default()
        assert SLAConcatenatedDetailsReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAConcatenatedDetailsReport.open_by_default()
        assert SLAConcatenatedDetailsReport.get_name_report() == SLAConcatenatedDetailsReport.name
