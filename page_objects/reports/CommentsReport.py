from ..BasePage import BasePage

class CommentsReport(BasePage):
    path = 'report/comments_report'

    _CHECK_REPORT = 'button[formaction="/report/comments_report/html"]'

    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
