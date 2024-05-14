from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class SLADynamicReport(BasePage):
    name = 'Динамика показателей по SLA'
    path = 'report/sla_dynamic_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/sla_dynamic_report/html"]')
    _LOCATOR_H2_NAME_REPORT = (By.XPATH, '//h2')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True

    def get_name_report(self) -> str:
        return self.find_element(self._LOCATOR_H2_NAME_REPORT).text
