

from ..BasePage import BasePage
import allure


class SubtasksDetailedReport(BasePage):
    path = 'report/subtasks_detailed_report'

    _CHECK_REPORT = 'button[formaction="/report/subtasks_detailed_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
