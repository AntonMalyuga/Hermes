import pytest

from page_objects.reports.NewPostmonReport import NewPostmonReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по фактическим доходам для Постмониторинга"')
@testit.description('Проверяется открытие отчёта "Отчёт по фактическим доходам для Постмониторинга"')
@pytest.mark.smoke
def test_open_report_new_postmon_report(driver):
    NewPostmonReport(driver).open()
    assert NewPostmonReport(driver).check_report()
