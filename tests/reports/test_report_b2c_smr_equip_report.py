import pytest

from page_objects.reports.B2CSmrEquipReport import B2CSmrEquipReport
import testit


class TestB2CSmrEquipReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CSmrEquipReport.open_by_default()
        assert B2CSmrEquipReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CSmrEquipReport.open_by_default()
        assert B2CSmrEquipReport.get_name_report() == B2CSmrEquipReport.name
