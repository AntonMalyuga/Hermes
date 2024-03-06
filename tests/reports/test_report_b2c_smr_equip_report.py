from page_objects.reports.B2CSmrEquipReport import B2CSmrEquipReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_smr_equip_report(driver):
    B2CSmrEquipReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CSmrEquipReport(driver).check_report()
