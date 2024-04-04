from page_objects.reports.InvestmentAllocation import InvestmentAllocation
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_investment_allocation(driver):
    InvestmentAllocation(driver).open()
    UserLoginForm(driver).authorization_default()
    assert InvestmentAllocation(driver).check_report()