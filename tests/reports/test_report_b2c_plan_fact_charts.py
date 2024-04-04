from page_objects.reports.B2CPlanFactCharts import B2CPlanFactCharts
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_plan_fact_charts(driver):
    B2CPlanFactCharts(driver).open()
    UserLoginForm(driver).authorization_default()
    assert B2CPlanFactCharts(driver).check_report()
