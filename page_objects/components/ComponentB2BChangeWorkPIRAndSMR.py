import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import testit


class ComponentB2BChangeWorkPIRAndSMR(BasePage):

    name = 'B2B: Редактировать объекмы работы ПИР/СМР'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_GROUP = (By.XPATH, _GROUP)
    _LOCATOR_BUTTON_FORM_WORK = (By.XPATH, f'{_GROUP}//a[text()="Редактировать объемы ПИР/СМР"]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def check_open_form(self):
        time.sleep(3)
        self.check_loader()
        if str(self.current_url()).find('volumes') != -1:
            return True
        else:
            raise ValueError(f'Получен некорректный URL, поиск значения "volumes" из {self.current_url()}')

    def open_form_work(self):
        with testit.step(f'Открыть форму "{self.name}"'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_FORM_WORK)
                link.click()
                self.check_open_form()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)
