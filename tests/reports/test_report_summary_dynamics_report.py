import allure

from page_objects.reports.SummaryDynamicsReport import SummaryDynamicsReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_summary_dynamics_report(driver):
    SummaryDynamicsReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SummaryDynamicsReport(driver).check_report()
