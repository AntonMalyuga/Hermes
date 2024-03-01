import allure

from page_objects.reports.ClaimsActivitiesReport import ClaimsActivitiesReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_claims_activities_report(driver):
    ClaimsActivitiesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert ClaimsActivitiesReport(driver).check_report()
