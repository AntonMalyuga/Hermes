from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class ComponentB2CChangeWorkPIRAndSMR(Order):
    name = 'B2C: Редактировать объекмы работы ПИР/СМР'

    _LOCATOR_BUTTON_FORM_WORK = 'a[href*="works_volumes"]')

    def open_form_work(self):
        with testit.step(f'Открыть форму "{self.name}"'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_FORM_WORK)
                link.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)
