from page_objects.reports.SLAContractorRatingReport import SLAContractorRatingReport
from page_objects.elements.UserLoginForm import UserLoginForm



def test_open_report_sla_contractor_rating_report(driver):
    SLAContractorRatingReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert SLAContractorRatingReport(driver).check_report()