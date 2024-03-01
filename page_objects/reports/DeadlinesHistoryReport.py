from ..BasePage import BasePage
import allure


class DeadlinesHistoryReport(BasePage):
    path = 'report/deadlines_history_report'

    _CHECK_REPORT = 'button[formaction="/report/deadlines_history_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True