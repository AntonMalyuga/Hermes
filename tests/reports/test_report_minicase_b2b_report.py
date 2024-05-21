import pytest

from page_objects.reports.MinicaseB2BReport import MinicaseB2BReport
import testit


class TestMinicaseB2BReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        MinicaseB2BReport.open_by_default()
        assert MinicaseB2BReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        MinicaseB2BReport.open_by_default()
        assert MinicaseB2BReport.get_name_report() == MinicaseB2BReport.name
