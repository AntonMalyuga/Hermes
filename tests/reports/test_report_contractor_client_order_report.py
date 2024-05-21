import pytest

from page_objects.reports.ContractorClientOrderReport import ContractorClientOrderReport
import testit


class TestContractorClientOrderReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        ContractorClientOrderReport.open_by_default()
        assert ContractorClientOrderReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        ContractorClientOrderReport.open_by_default()
        assert ContractorClientOrderReport.get_name_report() == ContractorClientOrderReport.name
