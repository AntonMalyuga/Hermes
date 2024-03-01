from ..BasePage import BasePage
import allure


class ComplexInstallationReport(BasePage):
    path = 'report/complex_installation_report'
    _CHECK_REPORT = 'button[formaction="/report/complex_installation_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
