import allure

from page_objects.reports.AggrClientProjectReport import AggrClientProjectReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_aggr_client_project_report(driver):
    AggrClientProjectReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert AggrClientProjectReport(driver).check_report()
