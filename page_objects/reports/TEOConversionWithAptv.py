from ..BasePage import BasePage
import allure


class TEOConversionWithAptv(BasePage):
    path = 'report/teo_conversion_with_aptv'

    _CHECK_REPORT = 'button[formaction="/report/teo_conversion_with_aptv/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True