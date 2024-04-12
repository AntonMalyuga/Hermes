from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class Hoz(Order):
    _LOCATOR_BUTTON_FORM_WORK = (By.CSS_SELECTOR, 'a[href*="works_volumes"]')
    _LOCATOR_BUTTON_FORM_SPECIFICATION = (By.CSS_SELECTOR, 'a[href*="specification"]')

    def open_form_work(self):
        with testit.step(f'Открыть рабочую форму'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_FORM_WORK)
                link.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)

    def open_form_specification(self):
        with testit.step(f'Открыть форму спецификации'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_FORM_SPECIFICATION)
                link.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)
