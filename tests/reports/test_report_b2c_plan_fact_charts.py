import allure

from page_objects.reports.B2CPlanFactCharts import B2CPlanFactCharts
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_plan_fact_charts(driver):
    B2CPlanFactCharts(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CPlanFactCharts(driver).check_report()
