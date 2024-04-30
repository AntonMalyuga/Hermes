from page_objects.reports.KS2ByWorkflow import KS2ByWorkflow
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по КС-2"')
@testit.description('Проверяется открытие отчёта "Отчёт по КС-2"')
def test_open_report_minicase_construct_dates_report(driver):
    KS2ByWorkflow(driver).open()
    UserLoginForm(driver).authorization_default()
    assert KS2ByWorkflow(driver).check_report()
