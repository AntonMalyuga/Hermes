from ..BasePage import BasePage
import allure


class MinicaseConstructDatesReport(BasePage):
    path = 'report/minicase_constructdates_report'

    _CHECK_REPORT = 'button[formaction="/report/minicase_constructdates_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
