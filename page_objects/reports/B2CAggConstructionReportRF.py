from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class B2CAggConstructionReportRF(BasePage):
    name = 'Сводный отчёт по строительству B2C'
    path = 'report/b2c_agg_construction_report_rf'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/b2c_agg_construction_report_rf/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
