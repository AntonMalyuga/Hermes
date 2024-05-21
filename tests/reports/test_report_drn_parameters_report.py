import pytest

from page_objects.reports.DrnParametersReport import DrnParametersReport
import testit


class TestDrnParametersReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        DrnParametersReport.open_by_default()
        assert DrnParametersReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        DrnParametersReport.open_by_default()
        assert DrnParametersReport.get_name_report() == DrnParametersReport.name
