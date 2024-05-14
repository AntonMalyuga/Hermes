from page_objects.reports.DrnParametersReport import DrnParametersReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по параметрам проекта по высвобождению недвижимости формируемый"')
@testit.description(
    'Проверяется открытие отчёта "Отчёт по параметрам проекта по высвобождению недвижимости формируемый"')
def test_open_report_drn_parameters_report(driver):
    DrnParametersReport(driver).open()
    assert DrnParametersReport(driver).check_report()
