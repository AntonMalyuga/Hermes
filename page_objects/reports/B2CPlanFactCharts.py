from ..BasePage import BasePage
import testit


class B2CPlanFactCharts(BasePage):
    path = 'report/b2c_plan_fact_charts'

    _CHECK_REPORT = 'button[formaction="/report/b2c_plan_fact_charts/xlsx"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
