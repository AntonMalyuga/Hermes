from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class TEOConversion(BasePage):
    name = 'Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости'
    path = 'report/teo_conversion'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/teo_conversion/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
