import allure

from page_objects.reports.SLAStagesReport import SLAStagesReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sla_stages_report(driver):
    SLAStagesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAStagesReport(driver).check_report()