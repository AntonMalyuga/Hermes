from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import testit


class B2CDepartmentsRating(BasePage):
    name = 'Рейтинг РФ по строительству B2C'
    path = 'report/b2c_departments_rating'

    _CHECK_REPORT = (By.CSS_SELECTOR, 'button[formaction="/report/b2c_departments_rating/html"]')

    def check_report(self):
        with testit.step(f'Проверить открытие отчета "{self.name}" по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
