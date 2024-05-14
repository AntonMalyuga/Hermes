import pytest

from page_objects.reports.B2CConstructionProjectMegaReport import B2CConstructionProjectMegaReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Мега отчёт по строительным проектам B2C"')
@testit.description('Проверить открытие отчёта "Мега отчёт по строительным проектам B2C"')
@pytest.mark.smoke
def test_open_report_b2c_construction_project_mega_report(driver):
    B2CConstructionProjectMegaReport(driver).open()
    assert B2CConstructionProjectMegaReport(driver).check_report()
