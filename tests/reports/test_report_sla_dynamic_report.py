import testit
import pytest
from page_objects.reports.SLADynamicReport import SLADynamicReport


class TestSLADynamicReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLADynamicReport.open_by_default()
        assert SLADynamicReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLADynamicReport.open_by_default()
        assert SLADynamicReport.get_name_report() == SLADynamicReport.name
