import allure

from page_objects.reports.SLADynamicReport import SLADynamicReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sla_dynamic_report(driver):
    SLADynamicReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLADynamicReport(driver).check_report()