import pytest

from page_objects.reports.DrnStagesReport import DrnStagesReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по этапам проекта по высвобождению недвижимости"')
@testit.description('Проверяется открытие отчёта "Отчёт по этапам проекта по высвобождению недвижимости"')
@pytest.mark.smoke
def test_open_report_drn_stages_report(driver):
    DrnStagesReport(driver).open()
    assert DrnStagesReport(driver).check_report()
