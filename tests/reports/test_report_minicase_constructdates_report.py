from page_objects.reports.MinicaseConstructDatesReport import MinicaseConstructDatesReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Постомониторинг аварийности"')
@testit.description('Проверяется открытие отчёта "Постомониторинг аварийности"')
def test_open_report_minicase_construct_dates_report(driver):
    MinicaseConstructDatesReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert MinicaseConstructDatesReport(driver).check_report()
