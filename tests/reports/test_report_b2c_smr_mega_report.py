import pytest
from page_objects.reports.B2CSmrMegaReport import B2CSmrMegaReport
import testit


class TestB2CSmrMegaReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CSmrMegaReport.open_by_default()
        assert B2CSmrMegaReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CSmrMegaReport.open_by_default()
        assert B2CSmrMegaReport.get_name_report() == B2CSmrMegaReport.name
