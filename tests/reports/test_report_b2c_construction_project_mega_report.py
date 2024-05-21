import pytest

from page_objects.reports.B2CConstructionProjectMegaReport import B2CConstructionProjectMegaReport
import testit


class TestB2CConstructionProjectMegaReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CConstructionProjectMegaReport.open_by_default()
        assert B2CConstructionProjectMegaReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CConstructionProjectMegaReport.open_by_default()
        assert B2CConstructionProjectMegaReport.get_name_report() == B2CConstructionProjectMegaReport.name
