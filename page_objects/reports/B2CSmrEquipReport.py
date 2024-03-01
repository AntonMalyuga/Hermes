from ..BasePage import BasePage
import allure


class B2CSmrEquipReport(BasePage):
    path = 'report/b2c_smr_equip_report'

    _CHECK_REPORT = 'button[formaction="/report/b2c_smr_equip_report/html"]'

    @allure.step('Проверить загрузку отчёта')
    def check_report(self):
        if len(self.find_elements(self._CHECK_REPORT)) > 0:
            return True
