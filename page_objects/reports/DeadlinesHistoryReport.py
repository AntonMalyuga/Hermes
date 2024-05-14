from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class DeadlinesHistoryReport(BasePage):
    name = 'Отчёт по переносу дат и сроков'
    path = 'report/deadlines_history_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/deadlines_history_report/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
