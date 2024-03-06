from page_objects.reports.RerInventoryNumbers import RerInventoryNumbers
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_rer_inventory_numbers(driver):
    RerInventoryNumbers(driver).open()
    UserLoginForm(driver).autorization_default()
    assert RerInventoryNumbers(driver).check_report()