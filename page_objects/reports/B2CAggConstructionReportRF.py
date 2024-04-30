from ..BasePage import BasePage
import testit


class B2CAggConstructionReportRF(BasePage):
    path = 'report/b2c_agg_construction_report_rf'

    _CHECK_REPORT = 'button[formaction="/report/b2c_agg_construction_report_rf/html"]'

    def check_report(self):
        with testit.step(f'Проверить открытие отчета по адресу "{self.path}", "Отчёт успешно открыт"'):
            if len(self.find_elements(self._CHECK_REPORT)) > 0:
                return True
