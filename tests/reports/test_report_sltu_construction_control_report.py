import allure

from page_objects.reports.SLTUConstructionControlReport import SLTUConstructionControlReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sltu_construction_control_report(driver):
    SLTUConstructionControlReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUConstructionControlReport(driver).check_report()
