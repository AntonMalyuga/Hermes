import allure

from page_objects.reports.SubtasksDetailedReport import SubtasksDetailedReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sltucontrol_det_expanded_report(driver):
    SubtasksDetailedReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SubtasksDetailedReport(driver).check_report()