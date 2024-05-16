import pytest
import testit

from page_objects.reports.ProjectAnalytics import ProjectAnalytics


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Аналитика проекта"')
@testit.description('Проверяется открытие отчёта "Аналитика проекта"')
@pytest.mark.smoke
def test_open_report_b2c_construction_project_mega_report(driver):
    ProjectAnalytics(driver).open()
    assert ProjectAnalytics(driver).check_report()
