from page_objects.reports.MinicaseB2BReport import MinicaseB2BReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по мини-кейсам B2B"')
@testit.description('Проверяется открытие отчёта "Отчёт по мини-кейсам B2B"')
def test_open_report_b2c_plan_fact_charts(driver):
    MinicaseB2BReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert MinicaseB2BReport(driver).check_report()
