import pytest
import testit

from page_objects.reports.SubtasksDetailedReport import SubtasksDetailedReport


class TestSubtasksDetailedReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        SubtasksDetailedReport.open_by_default()
        assert SubtasksDetailedReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        SubtasksDetailedReport.open_by_default()
        assert SubtasksDetailedReport.get_name_report() == SubtasksDetailedReport.name
