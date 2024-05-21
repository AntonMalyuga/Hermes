import pytest
import testit

from page_objects.reports.SLTUConstructionControlReport import SLTUConstructionControlReport


class TestSLTUConstructionControlReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SLTUConstructionControlReport.open_by_default()
        assert SLTUConstructionControlReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SLTUConstructionControlReport.open_by_default()
        assert SLTUConstructionControlReport.get_name_report() == SLTUConstructionControlReport.name
