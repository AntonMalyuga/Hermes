import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from pathlib import Path


class ComponentLoaderDH(Order):
    _LOCATOR_GROUP = (
        By.XPATH,
        '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]')
    _LOCATOR_YANDEX_LINK = (By.XPATH,
                            '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "yandex_constructor_link"]')
    _LOCATOR_SET_FILE_BUTTON = (By.XPATH,
                                '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@class= "form-control input-sm js--extract-file-name-on-change"]')
    _LOCATOR_LOAD_FILE_BUTTON = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//div[@class = "form-group"]//button[@type= "submit"]')

    def set_yandex_link(self, link):
        with testit.step(f'Set Yandex link {link} by component loader DH'):
            self.find_element(locator=self._LOCATOR_YANDEX_LINK).clear()
            self.find_element(locator=self._LOCATOR_YANDEX_LINK).send_keys(link)

    def set_file_path(self, file_name: str):
        with testit.step(f'Set file name {file_name} by component loader DH'):
            file_path = str(Path(__file__).resolve().parents[1].joinpath('b2c').joinpath('files').joinpath(file_name))
            self.find_element(self._LOCATOR_SET_FILE_BUTTON).send_keys(file_path)

    @testit.step('Submit by component loader DH')
    def push_set_file_button(self):
        self.find_element(locator=self._LOCATOR_LOAD_FILE_BUTTON).click()

    @testit.step('Move to group')
    def move_to_group(self):
        self.move_to_element(self._LOCATOR_GROUP)

    @testit.step('Add loader DH')
    def add_dh(self, link: str, file_name: str):
        self.check_loader()
        self.move_to_group()
        self.set_yandex_link(link)
        self.set_file_path(file_name)
        self.push_set_file_button()
