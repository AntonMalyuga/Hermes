from page_objects.reports.CommentsReport import CommentsReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по комментариям"')
@testit.description('Проверяется открытие отчёта "Отчёт по комментариям"')
def test_open_report_complex_installation_report(driver):
    CommentsReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert CommentsReport(driver).check_report()
