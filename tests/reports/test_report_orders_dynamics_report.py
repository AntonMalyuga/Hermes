import allure

from page_objects.reports.OrdersDynamicsReport import OrdersDynamicsReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_orders_dynamics_report(driver):
    OrdersDynamicsReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert OrdersDynamicsReport(driver).check_report()
