import pytest

from page_objects.reports.InvestmentAllocationConcatenatedDetails import InvestmentAllocationConcatenatedDetails
import testit


class TestInvestmentAllocationConcatenatedDetails:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        InvestmentAllocationConcatenatedDetails.open_by_default()
        assert InvestmentAllocationConcatenatedDetails.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        InvestmentAllocationConcatenatedDetails.open_by_default()
        assert InvestmentAllocationConcatenatedDetails.get_name_report() == InvestmentAllocationConcatenatedDetails.name
