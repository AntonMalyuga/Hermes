import allure

from page_objects.reports.DeadlinesHistoryReport import DeadlinesHistoryReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_deadlines_history_report(driver):
    DeadlinesHistoryReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert DeadlinesHistoryReport(driver).check_report()

