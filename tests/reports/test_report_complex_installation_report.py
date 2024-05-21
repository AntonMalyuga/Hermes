import pytest

from page_objects.reports.ComplexInstallationReport import ComplexInstallationReport
import testit


class TestComplexInstallationReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        ComplexInstallationReport.open_by_default()
        assert ComplexInstallationReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        ComplexInstallationReport.open_by_default()
        assert ComplexInstallationReport.get_name_report() == ComplexInstallationReport.name