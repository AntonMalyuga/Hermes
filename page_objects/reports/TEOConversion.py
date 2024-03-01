from ..BasePage import BasePage
import allure


class TEOConversion(BasePage):
    path = 'report/teo_conversion'

    _CHECK_REPORT = 'button[formaction="/report/teo_conversion/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True