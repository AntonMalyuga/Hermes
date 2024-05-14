import pytest

from page_objects.reports.ClaimsActivitiesReport import ClaimsActivitiesReport
import testit


@testit.title('reports')
@testit.displayName(
    'Проверить открытие отчёта "Отчёт для выявления фактов просрочки по стройке со стороны контрагентов"')
@testit.description(
    'Проверяется открытие отчёта "Отчёт для выявления фактов просрочки по стройке со стороны контрагентов"')
@pytest.mark.smoke
def test_open_report_claims_activities_report(driver):
    ClaimsActivitiesReport(driver).open()
    assert ClaimsActivitiesReport(driver).check_report()
