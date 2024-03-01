import allure

from page_objects.reports.LocalNormocontrolMega import LocalNormocontrolMega
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_local_normocontrol_mega(driver):
    LocalNormocontrolMega(driver).open()
    UserLoginForm(driver).autorization_default()
    assert LocalNormocontrolMega(driver).check_report()