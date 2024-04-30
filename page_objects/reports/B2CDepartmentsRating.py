from ..BasePage import BasePage
import testit


class B2CDepartmentsRating(BasePage):
    path = 'report/b2c_departments_rating'

    _CHECK_REPORT = 'button[formaction="/report/b2c_departments_rating/html"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
