from ..BasePage import BasePage

class SLAContractorRatingReport(BasePage):
    path = 'report/sla_contractor_rating_report'

    _CHECK_REPORT = 'button[formaction="/report/sla_contractor_rating_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True