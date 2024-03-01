import allure

from page_objects.reports.SLAContractorReport import SLAContractorReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sla_contractor_report(driver):
    SLAContractorReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAContractorReport(driver).check_report()