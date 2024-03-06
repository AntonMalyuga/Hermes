from ..BasePage import BasePage


class B2CConstructionProjectMegaReport(BasePage):
    path = 'report/b2c_construction_project_mega_report'

    _CHECK_REPORT = 'button[formaction="/report/b2c_construction_project_mega_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
