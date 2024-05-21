import pytest
import testit

from page_objects.reports.TEOConversion import TEOConversion


class TestTEOConversion:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        TEOConversion.open_by_default()
        assert TEOConversion.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        TEOConversion.open_by_default()
        assert TEOConversion.get_name_report() == TEOConversion.name
