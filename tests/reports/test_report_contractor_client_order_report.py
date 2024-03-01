import allure

from page_objects.reports.ContractorClientOrderReport import ContractorClientOrderReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_contractor_client_order_report(driver):
    ContractorClientOrderReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert ContractorClientOrderReport(driver).check_report()