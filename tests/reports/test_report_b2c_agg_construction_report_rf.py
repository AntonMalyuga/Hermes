import pytest

from page_objects.reports.B2CAggConstructionReportRF import B2CAggConstructionReportRF
import testit


class TestB2CAggConstructionReportRF:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CAggConstructionReportRF.open_by_default()
        assert B2CAggConstructionReportRF.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CAggConstructionReportRF.open_by_default()
        assert B2CAggConstructionReportRF.get_name_report() == B2CAggConstructionReportRF.name
