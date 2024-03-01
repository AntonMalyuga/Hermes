import allure

from page_objects.reports.NonSynchronizedPricesReport import NonSynchronizedPricesReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_agg_construction_report_rf(driver):
    NonSynchronizedPricesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert NonSynchronizedPricesReport(driver).check_report()
