from ..BasePage import BasePage
import allure


class SLAContractorReport(BasePage):
    path = 'report/sla_contractor_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_contractor_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True