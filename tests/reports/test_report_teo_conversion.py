import pytest
import testit

from page_objects.reports.TEOConversion import TEOConversion


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости"')
@testit.description('Проверяется открытие отчёта "Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости"')
@pytest.mark.smoke
def test_open_report_teo_conversion(driver):
    TEOConversion(driver).open()
    assert TEOConversion(driver).check_report()
