import allure

from page_objects.reports.B2CSmrMegaReport import B2CSmrMegaReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_smr_mega_report(driver):
    B2CSmrMegaReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CSmrMegaReport(driver).check_report()