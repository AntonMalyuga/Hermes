from ..BasePage import BasePage
import allure


class ClaimsActivitiesReport(BasePage):
    path = 'report/claims_activities_report'

    _CHECK_REPORT = 'button[formaction="/report/claims_activities_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
