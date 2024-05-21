import pytest
import testit

from page_objects.reports.TEOConversionWithAptv import TEOConversionWithAptv


class TestTEOConversionWithAptv:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        TEOConversionWithAptv.open_by_default()
        assert TEOConversionWithAptv.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        TEOConversionWithAptv.open_by_default()
        assert TEOConversionWithAptv.get_name_report() == TEOConversionWithAptv.name
