from page_objects.orders.Order import Order
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time


class B2CObjectOrder(Order):
    _LOCATOR_CHANGE_CONTRACTOR_BUTTON = (
        By.XPATH, '//button[@form[contains(., "form-change-client")]]')
    _LOCATOR_CONTRACTOR = (By.XPATH, '//div[@title = "Подрядчик"]')
    _LOCATOR_FRAME = (By.XPATH, '//input[@id[contains(., "contractorCode")]]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH, '//div[@class = "modal-footer"]/ancestor::div[2]//button[text() = "Сохранить"]')
    _LOCATOR_DISCOUNT = (By.XPATH, '//input[@name= "discount"]')
    _LOCATOR_SAVE_ORDER_BUTTON = (By.XPATH, '//div[@class= "row mb-10"]//button[@type = "submit"]')

    def _custom_select_method(self, locator, text):
        element = self.find_element(locator)
        locator_input = self.find_element((By.XPATH, f'{locator[1]}//input[@type="text"]'))
        element.click()
        locator_input.send_keys(text)
        time.sleep(1)
        locator_input.send_keys('\n')

    def push_change_contractor_button(self):
        self.find_element(locator=self._LOCATOR_CHANGE_CONTRACTOR_BUTTON).click()

    def set_contractor(self, contractor: str):
        time.sleep(2)
        keyboard = Controller()
        self._custom_select_method(locator=self._LOCATOR_CONTRACTOR, text=contractor)
        time.sleep(1)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    def set_frame(self, frame: int):
        time.sleep(2)
        self.find_element(locator=self._LOCATOR_FRAME).clear()
        self.find_element(locator=self._LOCATOR_FRAME).send_keys(frame)

    def push_save_contractor_button(self):
        self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    def set_discount(self, discount):
        self.find_element(locator=self._LOCATOR_DISCOUNT).clear()
        self.find_element(locator=self._LOCATOR_DISCOUNT).send_keys(discount)

    def push_save_order_button(self):
        self.find_element(locator=self._LOCATOR_SAVE_ORDER_BUTTON).click()

    def add_contractor(self, discount: int, contractor: str, frame: int):
        self.check_loader()
        self.push_change_contractor_button()
        self.set_contractor(contractor)
        self.set_frame(frame)
        self.push_save_contractor_button()
        self.check_loader()
        self.set_discount(discount)
        self.push_save_order_button()
