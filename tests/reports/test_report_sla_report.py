import allure

from page_objects.reports.SLAReport import SLAReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sla_report(driver):
    SLAReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAReport(driver).check_report()
