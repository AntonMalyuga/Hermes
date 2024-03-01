import allure

from page_objects.reports.MinicaseB2BServiceReport import MinicaseB2BServiceReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_plan_fact_charts(driver):
    MinicaseB2BServiceReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert MinicaseB2BServiceReport(driver).check_report()
