from page_objects.reports.NonSynchronizedPricesReport import NonSynchronizedPricesReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_agg_construction_report_rf(driver):
    NonSynchronizedPricesReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert NonSynchronizedPricesReport(driver).check_report()
