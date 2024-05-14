import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import testit


class ComponentB2BTransferWorkHoz(BasePage):
    name = 'B2B: Хоз. способ'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_GROUP = (By.XPATH, _GROUP)
    _LOCATOR_BUTTON_HOZ = (By.XPATH, '//a[text()="Хоз. способ"]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def check_open_form(self):
        time.sleep(3)
        self.check_loader()
        if str(self.current_url()).find('works') != -1:
            return True
        else:
            raise ValueError(f'Получен некорректный URL, поиск значения "volumes" из {self.current_url()}')

    def open_form_transfer_hoz_work(self):
        self.move_to_group()
        with testit.step(f'Открыть форму "{self.name}"'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_HOZ)
                link.click()
                self.check_open_form()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)
