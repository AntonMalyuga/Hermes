import pytest

from page_objects.reports.RerInventoryNumbers import RerInventoryNumbers
import testit


class TestRerInventoryNumbers:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        RerInventoryNumbers.open_by_default()
        assert RerInventoryNumbers.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        RerInventoryNumbers.open_by_default()
        assert RerInventoryNumbers.get_name_report() == RerInventoryNumbers.name
