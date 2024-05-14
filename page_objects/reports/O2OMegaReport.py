from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class O2OMegaReport(BasePage):
    name = 'Отчёт БП O2O'
    path = 'report/o2o_mega_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/o2o_mega_report/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
