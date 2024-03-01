import allure

from page_objects.reports.LocalClientOrderReport import LocalClientOrderReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_local_client_order_report(driver):
    LocalClientOrderReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert LocalClientOrderReport(driver).check_report()
