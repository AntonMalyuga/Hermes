
from page_objects.reports.TEOConversionWithAptv import TEOConversionWithAptv
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_teo_conversion_with_aptv(driver):
    TEOConversionWithAptv(driver).open()
    UserLoginForm(driver).autorization_default()
    assert TEOConversionWithAptv(driver).check_report()