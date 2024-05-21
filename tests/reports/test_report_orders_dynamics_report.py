import pytest

from page_objects.reports.OrdersDynamicsReport import OrdersDynamicsReport
import testit


class TestOrdersDynamicsReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        OrdersDynamicsReport.open_by_default()
        assert OrdersDynamicsReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        OrdersDynamicsReport.open_by_default()
        assert OrdersDynamicsReport.get_name_report() == OrdersDynamicsReport.name
