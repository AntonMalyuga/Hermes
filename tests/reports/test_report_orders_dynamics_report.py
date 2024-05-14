from page_objects.reports.OrdersDynamicsReport import OrdersDynamicsReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по динамике заявок за период"')
@testit.description('Проверяется открытие отчёта "Отчёт по динамике заявок за период"')
def test_open_report_orders_dynamics_report(driver):
    OrdersDynamicsReport(driver).open()
    assert OrdersDynamicsReport(driver).check_report()
