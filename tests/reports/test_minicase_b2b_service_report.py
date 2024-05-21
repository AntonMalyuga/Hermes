import pytest
import testit
from page_objects.reports.MinicaseB2BServiceReport import MinicaseB2BServiceReport


class TestMinicaseB2BServiceReport:

    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        MinicaseB2BServiceReport.open_by_default()
        assert MinicaseB2BServiceReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        MinicaseB2BServiceReport.open_by_default()
        assert MinicaseB2BServiceReport.get_name_report() == MinicaseB2BServiceReport.name
