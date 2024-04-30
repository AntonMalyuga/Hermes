from ..BasePage import BasePage
import testit


class DeadlinesHistoryReport(BasePage):
    path = 'report/deadlines_history_report'

    _CHECK_REPORT = 'button[formaction="/report/deadlines_history_report/html"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
