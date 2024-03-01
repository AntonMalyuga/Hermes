import allure

from page_objects.reports.InvestmentAllocation import InvestmentAllocation
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_investment_allocation(driver):
    InvestmentAllocation(driver).open()
    UserLoginForm(driver).autorization_default()
    assert InvestmentAllocation(driver).check_report()