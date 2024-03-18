import time

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ComponentNaturalIndicators(BasePage):
    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Натуральные показатели")]/ancestor::div[2]'
    _LOCATOR_BUTTON_OPEN_FORM = (By.XPATH, f'{_GROUP}//a[@title="Редактировать"]')
    _LOCATOR_BUTTON_SAVE = (By.XPATH, f'{_GROUP}//form//button[@type="submit"]')

    def open_editor(self):
        self.find_element(self._LOCATOR_BUTTON_OPEN_FORM).click()

    def set_natural_indicators_by_tpi(self, tpi_name: str, qty: int):
        locator = (By.XPATH, f'{self._GROUP}//table//tr[contains(., "{tpi_name}")]/ancestor::tr[1]//input')
        self.find_element(locator).send_keys(qty)


    def change_
    def save(self):
        self.find_element(self._LOCATOR_BUTTON_SAVE).click()
