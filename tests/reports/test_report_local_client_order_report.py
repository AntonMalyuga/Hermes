import pytest

from page_objects.reports.LocalClientOrderReport import LocalClientOrderReport
import testit


class TestLocalClientOrderReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        LocalClientOrderReport.open_by_default()
        assert LocalClientOrderReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        LocalClientOrderReport.open_by_default()
        assert LocalClientOrderReport.get_name_report() == LocalClientOrderReport.name
