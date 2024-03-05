from ..BasePage import BasePage
import allure


class RerSubtask(BasePage):
    path = 'report/rer_subtask'

    _CHECK_REPORT = 'button[formaction="/report/rer_subtask/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True