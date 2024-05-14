import pytest
import testit

from page_objects.reports.ProjectAnalytics import ProjectAnalytics
from page_objects.elements.UserLoginForm import UserLoginForm


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Аналитика проекта"')
@testit.description('Проверяется открытие отчёта "Аналитика проекта"')
@pytest.mark.smoke
def test_open_report_b2c_construction_project_mega_report(driver):
    ProjectAnalytics(driver).open()
    UserLoginForm(driver).authorization_default()
    assert ProjectAnalytics(driver).check_report()