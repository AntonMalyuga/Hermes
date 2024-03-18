import sys
from pathlib import Path
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order


class ComponentFiles(Order):
    _LOCATOR_GROUP = (By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Вложения")]')
    _FORM_ATTACHMENT = '//form[@action[contains(., "AddAttachment")]]'
    _LOCATOR_FORM_INPUT_FILE = (By.XPATH, f'{_FORM_ATTACHMENT}//input[@name[contains(., "file")]]')
    _LOCATOR_FORM_ATTACHMENT_TYPE = (By.XPATH, f'{_FORM_ATTACHMENT}//select[@id[contains(., "typeSelect")]]')
    _LOCATOR_FORM_ATTACHMENT_NAME = (By.XPATH, f'{_FORM_ATTACHMENT}//input[@id[contains(., "name")]]')
    _LOCATOR_FORM_ATTACHMENT_ADD_BUTTON = (By.XPATH, f'{_FORM_ATTACHMENT}//button[@type="submit"]')

    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)

    def add_file(self, name: str, type: str, file_name: str):
        self.check_loader()
        self.move_to_group()
        self.set_file_name(name)
        self.set_file_type(type)
        self.set_file_path(file_name)
        self.submit()

    def set_file_name(self, name: str):
        self.find_element(locator=self._LOCATOR_FORM_ATTACHMENT_NAME).send_keys(name)

    def set_file_type(self, type: str):

        self.check_open_order_interface()
        try:
            locator = (By.XPATH, f'{self._LOCATOR_FORM_ATTACHMENT_TYPE[1]}//option[contains(.,"{type}")]')
            self.find_element(locator=locator).click()
        except ValueError:
            raise f'Не найден тип вложения {type}'

    def set_file_path(self, file_name: str):
        file_path = str(Path(__file__).resolve().parents[1].joinpath('b2c').joinpath('files').joinpath(file_name))
        self.find_element(self._LOCATOR_FORM_INPUT_FILE).send_keys(file_path)

    def submit(self):
        self.find_element(self._LOCATOR_FORM_ATTACHMENT_ADD_BUTTON).click()
