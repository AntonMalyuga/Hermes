import pytest

from page_objects.reports.EmployeeReport import EmployeeReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по результатам работы сотрудников"')
@testit.description('Проверяется открытие отчёта "Отчёт по результатам работы сотрудников"')
@pytest.mark.smoke
def test_open_report_employee_report(driver):
    EmployeeReport(driver).open()
    assert EmployeeReport(driver).check_report()
