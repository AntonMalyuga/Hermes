from page_objects.reports.LocalNormocontrolMega import LocalNormocontrolMega
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_local_normocontrol_mega(driver):
    LocalNormocontrolMega(driver).open()
    UserLoginForm(driver).authorization_default()
    assert LocalNormocontrolMega(driver).check_report()