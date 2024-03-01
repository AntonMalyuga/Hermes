from ..BasePage import BasePage
import allure


class SLTUControlAggrReport(BasePage):
    path = 'report/sltucontrol_aggr_report'

    _CHECK_REPORT = 'button[formaction="/report/sltucontrol_aggr_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
