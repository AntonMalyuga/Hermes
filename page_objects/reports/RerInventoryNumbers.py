from ..BasePage import BasePage
import allure


class RerInventoryNumbers(BasePage):
    path = 'report/rer_inventory_numbers'

    _CHECK_REPORT = 'button[formaction="/report/rer_inventory_numbers/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True