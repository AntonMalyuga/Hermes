import pytest
import testit

from page_objects.reports.SLAContractorRatingReport import SLAContractorRatingReport


class TestSLAContractorRatingReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLAContractorRatingReport.open_by_default()
        assert SLAContractorRatingReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLAContractorRatingReport.open_by_default()
        assert SLAContractorRatingReport.get_name_report() == SLAContractorRatingReport.name
