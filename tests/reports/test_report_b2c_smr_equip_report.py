from page_objects.reports.B2CSmrEquipReport import B2CSmrEquipReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчет по оборудованию"')
@testit.description('Проверяется открытие отчёта "Отчет по оборудованию"')
def test_open_report_b2c_smr_equip_report(driver):
    B2CSmrEquipReport(driver).open()
    assert B2CSmrEquipReport(driver).check_report()
