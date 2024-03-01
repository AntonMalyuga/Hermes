import allure

from page_objects.reports.SLTUProcessingDetailedReport import SLTUProcessingDetailedReport
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_sltu_processing_detailed_report(driver):
    SLTUProcessingDetailedReport(driver).open()
    UserLoginForm(driver).autorization_default()
    assert SLTUProcessingDetailedReport(driver).check_report()
