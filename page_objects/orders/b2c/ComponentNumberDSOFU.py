import time
import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from pathlib import Path


class ComponentNumberDSOFU(Order):
    _LOCATOR_GROUP = (
        By.XPATH,
        '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//div[@class = "panel-heading binding-flag"]')
    _LOCATOR_EDIT_GLYF = (By.XPATH,
                          '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//a[@class = "js--load-element"]')
    _LOCATOR_IDENTIFY = (By.XPATH,
                         '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//input[@title = "идентификатор ДС ОФУ R12"]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH,
                              '//div[@class="panel panel-material"]//span[contains(., "Подрядчики")]/ancestor::div[2]//button[@type = "submit"]')

    def push_glyf(self):
        with testit.step(f'Нажать иконку открытия формы редактирования'):
            self.find_element(locator=self._LOCATOR_EDIT_GLYF).click()

    def set_identify_kode(self, kode):
        with testit.step(f'Ввести идентификационный код "{kode}"'):
            self.find_element(locator=self._LOCATOR_IDENTIFY).clear()
            self.find_element(locator=self._LOCATOR_IDENTIFY).send_keys(kode)

    def push_submit(self):
        with testit.step(f'Нажать кнопку сохранения'):
            self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def add_DSOFU(self, kode: int):
        with testit.step(f'Добавить ДСОФУ с кодом "{kode}"'):
            self.check_loader()
            self.move_to_group()
            self.push_glyf()
            self.check_loader()
            self.set_identify_kode(kode)
            self.push_submit()
            time.sleep(2)
