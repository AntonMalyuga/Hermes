import allure

from page_objects.reports.SLAContractorRatingReport import SLAContractorRatingReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sla_contractor_rating_report(driver):
    SLAContractorRatingReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAContractorRatingReport(driver).check_report()