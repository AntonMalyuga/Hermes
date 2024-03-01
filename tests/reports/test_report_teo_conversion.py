import allure

from page_objects.reports.TEOConversion import TEOConversion
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_teo_conversion(driver):
    TEOConversion(driver).open()
    UserLoginForm(driver).autorization_default()
    assert TEOConversion(driver).check_report()