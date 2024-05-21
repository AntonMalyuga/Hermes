import pytest
import testit

from page_objects.reports.ProjectAnalytics import ProjectAnalytics


class TestProjectAnalytics:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        ProjectAnalytics.open_by_default()
        assert ProjectAnalytics.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        ProjectAnalytics.open_by_default()
        assert ProjectAnalytics.get_name_report() == ProjectAnalytics.name
