import allure

from page_objects.reports.InvestmentAllocationConcatenatedDetails import InvestmentAllocationConcatenatedDetails
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_investment_allocation_concatenated_details(driver):
    InvestmentAllocationConcatenatedDetails(driver).open()
    UserLoginForm(driver).autorization_default()
    assert InvestmentAllocationConcatenatedDetails(driver).check_report()