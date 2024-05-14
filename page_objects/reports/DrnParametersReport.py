from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class DrnParametersReport(BasePage):
    name = 'Отчёт по параметрам проекта по высвобождению недвижимости формируемый'
    path = 'report/drn_parameters_report'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/drn_parameters_report/html"')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
