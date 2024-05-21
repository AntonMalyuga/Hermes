import pytest
import testit

from page_objects.reports.SLTUErrorsReport import SLTUErrorsReport


class TestSLTUErrorsReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUErrorsReport.open_by_default()
        assert SLTUErrorsReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUErrorsReport.open_by_default()
        assert SLTUErrorsReport.get_name_report() == SLTUErrorsReport.name
