from ..BasePage import BasePage
import allure


class SLTUProcessingDetailedReport(BasePage):
    path = 'report/sltu_processing_detailed_report'

    _CHECK_REPORT = 'button[formaction="/report/sltu_processing_detailed_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True