import pytest

from page_objects.reports.ExclusiveAddressesReport import ExclusiveAddressesReport
import testit


class TestExclusiveAddressesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        ExclusiveAddressesReport.open_by_default()
        assert ExclusiveAddressesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        ExclusiveAddressesReport.open_by_default()
        assert ExclusiveAddressesReport.get_name_report() == ExclusiveAddressesReport.name
