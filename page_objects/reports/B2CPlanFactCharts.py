from ..BasePage import BasePage
import allure


class B2CPlanFactCharts(BasePage):
    path = 'report/b2c_plan_fact_charts'

    _CHECK_REPORT = 'button[formaction="/report/b2c_plan_fact_charts/xlsx"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True