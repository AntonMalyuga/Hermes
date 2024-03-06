from ..BasePage import BasePage

class B2CDepartmentsRating(BasePage):
    path = 'report/b2c_departments_rating'

    _CHECK_REPORT = 'button[formaction="/report/b2c_departments_rating/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
