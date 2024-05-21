import pytest

from page_objects.reports.MinicaseConstructDatesReport import MinicaseConstructDatesReport
import testit


class TestMinicaseConstructDatesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        MinicaseConstructDatesReport.open_by_default()
        assert MinicaseConstructDatesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        MinicaseConstructDatesReport.open_by_default()
        assert MinicaseConstructDatesReport.get_name_report() == MinicaseConstructDatesReport.name
