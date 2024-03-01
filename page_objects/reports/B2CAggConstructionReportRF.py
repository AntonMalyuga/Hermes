from ..BasePage import BasePage
import allure


class B2CAggConstructionReportRF(BasePage):
    path = 'report/b2c_agg_construction_report_rf'

    _CHECK_REPORT = 'button[formaction="/report/b2c_agg_construction_report_rf/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
