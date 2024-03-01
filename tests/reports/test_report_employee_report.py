import allure

from page_objects.reports.EmployeeReport import EmployeeReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_employee_report(driver):
    EmployeeReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert EmployeeReport(driver).check_report()