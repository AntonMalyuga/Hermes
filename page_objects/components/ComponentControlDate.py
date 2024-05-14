from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class ComponentControlDate(Order):

    name = 'B2C: Контрольные даты'

    _LOCATOR_GROUP = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Контрольные даты")]/ancestor::div[2]')
    _LOCATOR_BUTTON_CHANGE_ALL_CONTROL_DATES = (By.XPATH, '//div[@id[contains(., "btn-editor-control-dates")]]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def change_all_control_dates(self, cnt_dates: int):
        with testit.step(f'Изменить контрольные даты "{cnt_dates}"'):
            self.check_loader()
            self.move_to_group()
            component = self._LOCATOR_BUTTON_CHANGE_ALL_CONTROL_DATES[1]
            self.find_element((By.XPATH, f'{component}//button[@class[contains(., "btn-default")]]')).click()
            self.find_element(
                (By.XPATH, f'//div[@id[contains(., "editor-control-dates")]]//input[@type="text"]')).send_keys(
                cnt_dates)
            self.find_element(
                (By.XPATH, f'//div[@id[contains(., "editor-control-dates")]]//button[@type="submit"]')).click()
