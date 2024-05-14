from page_objects.reports.MinicaseB2BServiceReport import MinicaseB2BServiceReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по услугам мини-кейса B2B"')
@testit.description('Проверяется открытие отчёта "Отчёт по услугам мини-кейса B2B"')
def test_open_report_b2c_plan_fact_charts(driver):
    MinicaseB2BServiceReport(driver).open()
    assert MinicaseB2BServiceReport(driver).check_report()
