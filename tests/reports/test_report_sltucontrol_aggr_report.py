import allure

from page_objects.reports.SLTUControlAggrReport import SLTUControlAggrReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sltucontrol_aggr_report(driver):
    SLTUControlAggrReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUControlAggrReport(driver).check_report()
