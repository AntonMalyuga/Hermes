from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class ComponentChangeSpecification(Order):
    name = 'Редактировать спецификацию оборудования'

    _LOCATOR_BUTTON_FORM_SPECIFICATION = (By.CSS_SELECTOR, 'a[href*="specification"]')

    def open_form_specification(self):
        with testit.step(f'Открыть форму спецификации'):
            self.check_loader()
            try:
                link = self.find_element(locator=self._LOCATOR_BUTTON_FORM_SPECIFICATION)
                link.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", link)
