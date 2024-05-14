import testit

from page_objects.reports.TEOConversionWithAptv import TEOConversionWithAptv


@testit.title('reports')
@testit.displayName(
    'Проверить открытие отчёта "Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости и с аналитикой АПТВ"')
@testit.description(
    'Проверяется открытие отчёта "Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости и с аналитикой АПТВ"')
def test_open_report_teo_conversion_with_aptv(driver):
    TEOConversionWithAptv(driver).open()
    assert TEOConversionWithAptv(driver).check_report()
