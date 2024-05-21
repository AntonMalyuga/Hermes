import pytest
import testit

from page_objects.reports.SLTUBookingReport import SLTUBookingReport


class TestSLTUBookingReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUBookingReport.open_by_default()
        assert SLTUBookingReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUBookingReport.open_by_default()
        assert SLTUBookingReport.get_name_report() == SLTUBookingReport.name
