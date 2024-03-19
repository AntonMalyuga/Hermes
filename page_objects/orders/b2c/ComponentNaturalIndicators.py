from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.common.keys import Keys
import random


class ComponentNaturalIndicator(Order):
    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Натуральные показатели")]/ancestor::div[2]'
    _COMPONENT_BUTTON_OPEN_EDITOR = (By.XPATH, f'{_GROUP}//a[@title="Редактировать"]')
    _COMPONENT_BUTTON_SAVE = (By.XPATH, f'{_GROUP}//button[@type="submit"]')

    def move_to_group(self):
        self.move_to_element((By.XPATH, self._GROUP))

    def open_editor(self):
        self.find_element(self._COMPONENT_BUTTON_OPEN_EDITOR).click()

    def set_random_qty(self):
        locator = f'{self._GROUP}//input[@type="number"]'
        inputs = self.find_elements(locator=(By.XPATH, locator))

        for input_element in inputs:
            input_element.send_keys(Keys.CONTROL, 'a')
            input_element.send_keys(Keys.BACKSPACE)
            input_element.send_keys(random.randint(1, 9))

    def save(self):
        self.find_element(self._COMPONENT_BUTTON_SAVE).click()

    def add_random(self):
        self.check_loader()
        self.move_to_group()
        self.open_editor()
        self.set_random_qty()
        self.save()
