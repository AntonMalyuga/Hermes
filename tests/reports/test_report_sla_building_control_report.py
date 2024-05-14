import pytest
import testit

from page_objects.reports.SLABuildingControlReport import SLABuildingControlReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Контроль стройки"')
@testit.description('Проверяется открытие отчёта "Контроль стройки"')
@pytest.mark.smoke
def test_open_report_sla_building_control_report(driver):
    SLABuildingControlReport(driver).open()
    assert SLABuildingControlReport(driver).check_report()
