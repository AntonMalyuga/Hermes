import pytest

from page_objects.reports.MinicaseConstructDatesReport import MinicaseConstructDatesReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Постомониторинг аварийности"')
@testit.description('Проверяется открытие отчёта "Постомониторинг аварийности"')
@pytest.mark.smoke
def test_open_report_minicase_construct_dates_report(driver):
    MinicaseConstructDatesReport(driver).open()
    assert MinicaseConstructDatesReport(driver).check_report()
