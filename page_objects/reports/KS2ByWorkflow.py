from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class KS2ByWorkflow(BasePage):
    name = 'Отчёт по КС-2'
    path = 'report/ks2_by_workflow'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/ks2_by_workflow/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
