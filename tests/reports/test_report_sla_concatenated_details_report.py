import allure

from page_objects.reports.SLAConcatenatedDetailsReport import SLAConcatenatedDetailsReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_rer_subtask(driver):
    SLAConcatenatedDetailsReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLAConcatenatedDetailsReport(driver).check_report()
