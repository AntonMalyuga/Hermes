import allure

from page_objects.reports.ProjectAnalytics import ProjectAnalytics
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_construction_project_mega_report(driver):
    ProjectAnalytics(driver).open()
    UserLoginForm(driver).autorization_default()
    assert ProjectAnalytics(driver).check_report()