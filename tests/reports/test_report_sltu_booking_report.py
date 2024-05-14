import testit

from page_objects.reports.SLTUBookingReport import SLTUBookingReport


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Отчёт по запросам бронирования в шину"')
@testit.description('Проверяется открытие отчёта "Отчёт по запросам бронирования в шину"')
def test_open_report_sltu_booking_report(driver):
    SLTUBookingReport(driver).open()
    assert SLTUBookingReport(driver).check_report()
