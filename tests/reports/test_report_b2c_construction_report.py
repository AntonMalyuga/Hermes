import pytest
import testit
from page_objects.reports.B2CConstructionReport import B2CConstructionReport


class TestB2CConstructionReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CConstructionReport.open_by_default()
        assert B2CConstructionReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CConstructionReport.open_by_default()
        assert B2CConstructionReport.get_name_report() == B2CConstructionReport.name
