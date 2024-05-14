from page_objects.reports.MinicaseB2BReport import MinicaseB2BReport
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по мини-кейсам B2B"')
@testit.description('Проверяется открытие отчёта "Отчёт по мини-кейсам B2B"')
def test_open_report_b2c_plan_fact_charts(driver):
    MinicaseB2BReport(driver).open()
    assert MinicaseB2BReport(driver).check_report()
