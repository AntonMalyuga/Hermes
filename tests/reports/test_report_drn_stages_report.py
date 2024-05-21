import pytest

from page_objects.reports.DrnStagesReport import DrnStagesReport
import testit


class TestDrnStagesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        DrnStagesReport.open_by_default()
        assert DrnStagesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        DrnStagesReport.open_by_default()
        assert DrnStagesReport.get_name_report() == DrnStagesReport.name
