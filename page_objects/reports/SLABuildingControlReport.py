from ..BasePage import BasePage
import allure


class SLABuildingControlReport(BasePage):
    path = 'report/sla_building_control_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_building_control_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True