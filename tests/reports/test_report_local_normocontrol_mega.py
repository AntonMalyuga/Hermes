from page_objects.reports.LocalNormocontrolMega import LocalNormocontrolMega
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Нормоконтроль (формируемый)"')
@testit.description('Проверяется открытие отчёта "Нормоконтроль (формируемый)"')
def test_open_report_local_normocontrol_mega(driver):
    LocalNormocontrolMega(driver).open()
    assert LocalNormocontrolMega(driver).check_report()
