from ..BasePage import BasePage
import allure


class ExclusiveAddressesReport(BasePage):
    path = 'report/exclusive_addresses_report'

    _CHECK_REPORT = 'button[formaction="/report/exclusive_addresses_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True