import testit

from page_objects.reports.SubtasksDetailedReport import SubtasksDetailedReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Детальный отчёт по подзадачам"')
@testit.description('Проверяется открытие отчёта "Детальный отчёт по подзадачам"')
def test_open_report_sltucontrol_det_expanded_report(driver):
    SubtasksDetailedReport(driver).open()
    assert SubtasksDetailedReport(driver).check_report()
