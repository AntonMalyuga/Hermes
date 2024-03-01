from ..BasePage import BasePage
import allure


class NewPostmonReport(BasePage):
    path = 'report/new_postmon_report'
    _CHECK_REPORT = 'button[formaction="/report/new_postmon_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
