import pytest
import testit

from page_objects.reports.SLTUControlAggrReport import SLTUControlAggrReport


class TestSLTUControlAggrReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUControlAggrReport.open_by_default()
        assert SLTUControlAggrReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUControlAggrReport.open_by_default()
        assert SLTUControlAggrReport.get_name_report() == SLTUControlAggrReport.name
