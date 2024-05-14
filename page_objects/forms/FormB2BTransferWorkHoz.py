from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.BasePage import BasePage
import testit


class FormB2BTransferWorkHoz(BasePage):
    name = 'B2B: Выбор работ хоз. способом'

    _LOCATOR_CHECKBOX_TRANSFER_HOZ = (
    By.XPATH, '//form[contains(@action,"works")]//input[@type="checkbox"]//following::label[1]')
    _LOCATOR_BTN_SAVE = (By.XPATH, '//form[contains(@action,"works")]//button[@type="submit"]')
    _LOCATOR_DIV_CHECK_CHANGES = (By.XPATH, '//div[@class="alert alert-success alert-dismissable"]')

    def get_all_switch_hoz(self) -> list[WebElement]:
        return self.find_elements(self._LOCATOR_CHECKBOX_TRANSFER_HOZ)

    def save(self):
        self.find_element(self._LOCATOR_BTN_SAVE).click()

    def check_save_changes(self):
        if self.find_element(self._LOCATOR_DIV_CHECK_CHANGES).is_enabled():
            return True
        else:
            raise Exception('Работы не перенесены')

    def set_all_works_hoz(self):
        for switch in self.get_all_switch_hoz():
            switch.click()
        self.save()
        self.check_save_changes()
        self.close()
