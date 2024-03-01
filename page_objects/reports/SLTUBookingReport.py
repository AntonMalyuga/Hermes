from ..BasePage import BasePage
import allure


class SLTUBookingReport(BasePage):
    path = 'report/sltu_booking_report'

    _CHECK_REPORT = 'button[formaction="/report/sltu_booking_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True