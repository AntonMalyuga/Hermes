import pytest
import testit

from page_objects.reports.SLABuildingControlReport import SLABuildingControlReport


class TestSLABuildingControlReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLABuildingControlReport.open_by_default()
        assert SLABuildingControlReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLABuildingControlReport.open_by_default()
        assert SLABuildingControlReport.get_name_report() == SLABuildingControlReport.name
