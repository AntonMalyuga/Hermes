from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class LocalNormocontrolMega(BasePage):
    name = 'Нормоконтроль (формируемый)'
    path = 'report/localnormocontrolmega'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/localnormocontrolmega/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
