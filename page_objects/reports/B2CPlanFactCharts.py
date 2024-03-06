from ..BasePage import BasePage

class B2CPlanFactCharts(BasePage):
    path = 'report/b2c_plan_fact_charts'

    _CHECK_REPORT = 'button[formaction="/report/b2c_plan_fact_charts/xlsx"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True