from page_objects.reports.DeadlinesHistoryReport import DeadlinesHistoryReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по переносу дат и сроков"')
@testit.description('Проверяется открытие отчёта "Отчёт по переносу дат и сроков"')
def test_open_report_deadlines_history_report(driver):
    DeadlinesHistoryReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert DeadlinesHistoryReport(driver).check_report()
