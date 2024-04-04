from page_objects.reports.DeadlinesHistoryReport import DeadlinesHistoryReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_deadlines_history_report(driver):
    DeadlinesHistoryReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert DeadlinesHistoryReport(driver).check_report()

