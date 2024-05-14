import time
import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ComponentLinkSip(Order):

    name = 'B2C: Ссылка на карточку ИП в СИП'

    _LOCATOR_GROUP = (
        By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]')
    _LOCATOR_EDIT_FORM_BUTTON_CART = (By.XPATH,
                                      '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "clearfix agg-caption"]//a[@title = "Редактировать"]')
    _LOCATOR_B2C_LIP_FIELD = (By.XPATH,
                              '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[2]"]')
    _LOCATOR_B2C_KIP_CORE_FIELD = (By.XPATH,
                                   '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[3]"]')
    _LOCATOR_B2C_KIP_KEY_FIELD = (By.XPATH,
                                  '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//input[@name= "type[4]"]')
    _LOCATOR_CART_SUBMIT_BUTTON = (By.XPATH,
                                   '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//form[@class = "form js--load-element"]//button[@type = "submit"]')

    def push_edit_cart_form_button(self):
        with testit.step(f'Нажать кнопку редактирования карточки', 'Кнопка нажата'):
            self.find_element(locator=self._LOCATOR_EDIT_FORM_BUTTON_CART).click()

    def fill_select_type_field(self, value):
        with testit.step(f'Заполнить поле выбора типа "{value}"'):
            select = Select(self.find_element(locator=self._LOCATOR_SELECT_TYPE_FIELD))
            select.select_by_visible_text(value)

    def change_link_sip(self, lip, kip, kip_key):
        with testit.step(f'Выбрать ссылку СИП: ЛИП "{lip}", КИП "{kip}" или ключ КИП "{kip_key}"'):
            self.clean_strings(self._LOCATOR_B2C_LIP_FIELD)
            self.clean_strings(self._LOCATOR_B2C_KIP_CORE_FIELD)
            self.clean_strings(self._LOCATOR_B2C_KIP_KEY_FIELD)
            if lip == "" and kip == "" and kip_key == "":
                raise 'Не введены значения'

            if lip != "":
                self.clean_strings(self._LOCATOR_B2C_LIP_FIELD)
                self.insert(self._LOCATOR_B2C_LIP_FIELD, lip)
            if kip != "":
                self.clean_strings(self._LOCATOR_B2C_KIP_CORE_FIELD)
                self.insert(self._LOCATOR_B2C_KIP_CORE_FIELD, kip)
            if kip_key != "":
                self.clean_strings(self._LOCATOR_B2C_KIP_KEY_FIELD)
                self.insert(self._LOCATOR_B2C_KIP_KEY_FIELD, kip_key)

    def insert(self, input_locator, value):
        with testit.step(f'Ввести значение "{value}"'):
            self.find_element(locator=input_locator).send_keys(Keys.CONTROL, 'a')
            self.find_element(locator=input_locator).send_keys(value)

    def clean_strings(self, locator):
        with testit.step(f'Очистить строку'):
            self.find_element(locator=locator).send_keys(Keys.CONTROL, 'a')
            self.find_element(locator=locator).send_keys(Keys.BACKSPACE)

    def push_cart_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения'):
            self.find_element(locator=self._LOCATOR_CART_SUBMIT_BUTTON).click()

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def add_link_sip(self, lip: str, kip: str, kip_key: str):
        with testit.step(f'Добавить ссылку СИП: ЛИП "{lip}", КИП "{kip}" или ключ КИП "{kip_key}"'):
            self.check_loader()
            self.move_to_group()
            self.push_edit_cart_form_button()
            self.change_link_sip(lip, kip, kip_key)
            self.push_cart_submit_button()
