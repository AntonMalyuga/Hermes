from ..BasePage import BasePage
import allure


class ProjectAnalytics(BasePage):
    path = 'report/projectanalytics'
    _CHECK_REPORT = 'button[formaction="/report/projectanalytics/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
