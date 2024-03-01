import allure

from page_objects.reports.B2CConstructionReport import B2CConstructionReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_construction_report(driver):
    B2CConstructionReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CConstructionReport(driver).check_report()
