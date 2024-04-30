from page_objects.reports.DrnStagesReport import DrnStagesReport
from page_objects.elements.UserLoginForm import UserLoginForm
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по этапам проекта по высвобождению недвижимости"')
@testit.description('Проверяется открытие отчёта "Отчёт по этапам проекта по высвобождению недвижимости"')
def test_open_report_drn_stages_report(driver):
    DrnStagesReport(driver).open()
    UserLoginForm(driver).authorization_default()
    assert DrnStagesReport(driver).check_report()
