import pytest

from page_objects.reports.InvestmentAllocation import InvestmentAllocation
import testit


class TestInvestmentAllocation:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        InvestmentAllocation.open_by_default()
        assert InvestmentAllocation.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        InvestmentAllocation.open_by_default()
        assert InvestmentAllocation.get_name_report() == InvestmentAllocation.name
