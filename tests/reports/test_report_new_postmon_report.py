import pytest

from page_objects.reports.NewPostmonReport import NewPostmonReport
import testit


class TestNewPostmonReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        NewPostmonReport.open_by_default()
        assert NewPostmonReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        NewPostmonReport.open_by_default()
        assert NewPostmonReport.get_name_report() == NewPostmonReport.name
