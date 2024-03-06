from page_objects.reports.ExclusiveAddressesReport import ExclusiveAddressesReport
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_investment_allocation_concatenated_details(driver):
    ExclusiveAddressesReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert ExclusiveAddressesReport(driver).check_report()