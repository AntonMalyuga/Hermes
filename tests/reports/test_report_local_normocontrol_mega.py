import pytest

from page_objects.reports.LocalNormocontrolMega import LocalNormocontrolMega
import testit


class TestLocalNormocontrolMega:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        LocalNormocontrolMega.open_by_default()
        assert LocalNormocontrolMega.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        LocalNormocontrolMega.open_by_default()
        assert LocalNormocontrolMega.get_name_report() == LocalNormocontrolMega.name
