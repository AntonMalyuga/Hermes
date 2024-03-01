import allure

from page_objects.reports.DrnParametersReport import DrnParametersReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_drn_parameters_report(driver):
    DrnParametersReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert DrnParametersReport(driver).check_report()