import pytest

from page_objects.reports.B2CPlanFactCharts import B2CPlanFactCharts
import testit


class TestB2CPlanFactCharts:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CPlanFactCharts.open_by_default()
        assert B2CPlanFactCharts.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CPlanFactCharts.open_by_default()
        assert B2CPlanFactCharts.get_name_report() == B2CPlanFactCharts.name
