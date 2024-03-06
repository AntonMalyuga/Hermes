from page_objects.reports.RerSubtask import RerSubtask
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_report_rer_subtask(driver):
    RerSubtask(driver).open()
    UserLoginForm(driver).autorization_default()
    assert RerSubtask(driver).check_report()
