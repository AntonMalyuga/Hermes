from page_objects.reports.ClaimsActivitiesReport import ClaimsActivitiesReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName(
    'Проверить открытие отчёта "Отчёт для выявления фактов просрочки по стройке со стороны контрагентов"')
@testit.description(
    'Проверяется открытие отчёта "Отчёт для выявления фактов просрочки по стройке со стороны контрагентов"')
def test_open_report_claims_activities_report(driver):
    ClaimsActivitiesReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert ClaimsActivitiesReport(driver).check_report()
