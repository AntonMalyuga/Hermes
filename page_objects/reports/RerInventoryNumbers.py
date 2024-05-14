from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class RerInventoryNumbers(BasePage):
    name = 'Отчет по инвентарным номерам'
    path = 'report/rer_inventory_numbers'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/rer_inventory_numbers/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
