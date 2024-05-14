from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class SLAReportByStages(BasePage):
    name = 'Отчёт о результатах работы по SLA по этапам'
    path = 'report/sla_report_by_stages'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/sla_report_by_stages/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
