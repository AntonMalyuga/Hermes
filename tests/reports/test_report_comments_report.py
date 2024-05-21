import pytest

from page_objects.reports.CommentsReport import CommentsReport
import testit


class TestCommentsReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        CommentsReport.open_by_default()
        assert CommentsReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        CommentsReport.open_by_default()
        assert CommentsReport.get_name_report() == CommentsReport.name
