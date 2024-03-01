import allure

from page_objects.reports.SLTUBookingReport import SLTUBookingReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sltu_booking_report(driver):
    SLTUBookingReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUBookingReport(driver).check_report()
