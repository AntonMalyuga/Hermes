import pytest
import testit

from page_objects.reports.SLTUControlDetReport import SLTUControlDetReport


class TestSLTUControlDetReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUControlDetReport.open_by_default()
        assert SLTUControlDetReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUControlDetReport.open_by_default()
        assert SLTUControlDetReport.get_name_report() == SLTUControlDetReport.name
