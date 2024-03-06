from page_objects.reports.B2CAggConstructionReportRF import B2CAggConstructionReportRF
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_b2c_agg_construction_report_rf(driver):
    B2CAggConstructionReportRF(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CAggConstructionReportRF(driver).check_report()
