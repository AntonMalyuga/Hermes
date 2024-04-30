from page_objects.reports.EmployeeReport import EmployeeReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по результатам работы сотрудников"')
@testit.description('Проверяется открытие отчёта "Отчёт по результатам работы сотрудников"')
def test_open_report_employee_report(driver):
    EmployeeReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert EmployeeReport(driver).check_report()
