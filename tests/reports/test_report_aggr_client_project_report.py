from page_objects.reports.AggrClientProjectReport import AggrClientProjectReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Агрегированная Аналитика проекта"')
@testit.description('Проверяется открытие отчёта "Агрегированная Аналитика проекта"')
def test_open_report_aggr_client_project_report(driver):
    AggrClientProjectReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert AggrClientProjectReport(driver).check_report()
