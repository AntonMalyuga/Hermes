from ..BasePage import BasePage
import allure


class SummaryDynamicsReport(BasePage):
    path = 'report/summary_dynamics_report'

    _CHECK_REPORT = 'button[formaction="/report/summary_dynamics_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
