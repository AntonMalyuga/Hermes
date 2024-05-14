import pytest
import testit

from page_objects.reports.SLAConcatenatedDetailsReport import SLAConcatenatedDetailsReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Соединенный Детальный отчёт о результатах работы по SLA"')
@testit.description('Проверяется открытие отчёта "Соединенный Детальный отчёт о результатах работы по SLA"')
@pytest.mark.smoke
def test_open_report_rer_subtask(driver):
    SLAConcatenatedDetailsReport(driver).open()
    assert SLAConcatenatedDetailsReport(driver).check_report()
