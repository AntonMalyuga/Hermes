from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class SLTUControlDetReport(BasePage):
    name = 'Детальный Отчёт по контролю корректности данных в СЛТУ'
    path = 'report/sltucontrol_det_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/sltucontrol_det_report/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
