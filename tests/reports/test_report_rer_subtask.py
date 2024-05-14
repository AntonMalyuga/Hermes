import pytest
import testit

from page_objects.reports.RerSubtask import RerSubtask


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный отчёт по подзадачам"')
@testit.description('Проверяется открытие отчёта "Детальный отчёт по подзадачам"')
@pytest.mark.smoke
def test_open_report_rer_subtask(driver):
    RerSubtask(driver).open()
    assert RerSubtask(driver).check_report()
