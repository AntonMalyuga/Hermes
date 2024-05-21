import pytest

from page_objects.reports.ClaimsActivitiesReport import ClaimsActivitiesReport
import testit


class TestClaimsActivitiesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        ClaimsActivitiesReport.open_by_default()
        assert ClaimsActivitiesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        ClaimsActivitiesReport.open_by_default()
        assert ClaimsActivitiesReport.get_name_report() == ClaimsActivitiesReport.name
