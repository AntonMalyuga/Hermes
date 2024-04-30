from ..BasePage import BasePage
import testit


class LocalClientOrderReport(BasePage):
    path = 'report/local_client_order_report'
    _CHECK_REPORT = 'button[formaction="/report/local_client_order_report/html"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
