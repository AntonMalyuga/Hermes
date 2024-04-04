from page_objects.reports.OrdersDynamicsReport import OrdersDynamicsReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_orders_dynamics_report(driver):
    OrdersDynamicsReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert OrdersDynamicsReport(driver).check_report()
