from page_objects.reports.SLTUErrorsReport import SLTUErrorsReport
from page_objects.elements.UserLoginForm import UserLoginForm




def test_open_report_b2c_departments_rating(driver):
    SLTUErrorsReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUErrorsReport(driver).check_report()
