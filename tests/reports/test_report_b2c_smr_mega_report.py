import pytest

from page_objects.reports.B2CSmrMegaReport import B2CSmrMegaReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Мега отчёт по объектам B2C"')
@testit.description('Проверяется открытие отчёта "Мега отчёт по объектам B2C"')
@pytest.mark.smoke
def test_open_report_b2c_smr_mega_report(driver):
    B2CSmrMegaReport(driver).open()
    assert B2CSmrMegaReport(driver).check_report()
