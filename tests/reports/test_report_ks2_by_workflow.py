import allure

from page_objects.reports.KS2ByWorkflow import KS2ByWorkflow
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_minicase_construct_dates_report(driver):
    KS2ByWorkflow(driver).open()
    UserLoginForm(driver).autorization_default()
    assert KS2ByWorkflow(driver).check_report()
