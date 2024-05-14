from page_objects.orders.Order import Order
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
import testit


class FormB2CObjectOrder(Order):

    name = 'Объекты заказа КИП'
    path = 'b2c/group_orders'

    _ORDER_ID = (By.CSS_SELECTOR, '.form-group.mb-0 .js--load-tab.js--new-tab')
    _LOCATOR_CHANGE_CONTRACTOR_BUTTON = (
        By.XPATH, '//button[@form[contains(., "form-change-client")]]')
    _LOCATOR_CONTRACTOR = (By.XPATH, '//div[@title = "Подрядчик"]')
    _LOCATOR_FRAME = (By.XPATH, '//input[@id[contains(., "contractorCode")]]')
    _LOCATOR_SUBMIT_BUTTON = (By.XPATH, '//div[@class = "modal-footer"]/ancestor::div[2]//button[text() = "Сохранить"]')
    _LOCATOR_DISCOUNT = (By.XPATH, '//input[@name= "discount"]')
    _LOCATOR_SAVE_ORDER_BUTTON = (By.XPATH, '//div[@class= "row mb-10"]//button[@type = "submit"]')

    @testit.step('Open form object contract KIP by order {order}')
    def open_form(self, order_id):
        self.open_for_path(f'/{order_id}')

    @testit.step('Get order id in form object contract KIP')
    def get_custom_order_order_id(self):
        return int(str(self.find_element(locator=self._ORDER_ID).text).strip())

    @testit.step('Custom select form object contract KIP by {locator} and text {text}')
    def _custom_select_method(self, locator, text):
        element = self.find_element(locator)
        locator_input = self.find_element((By.XPATH, f'{locator[1]}//input[@type="text"]'))
        element.click()
        locator_input.send_keys(text)
        time.sleep(1)
        locator_input.send_keys('\n')

    @testit.step('Click change contractor in form object contract KIP')
    def push_change_contractor_button(self):
        self.find_element(locator=self._LOCATOR_CHANGE_CONTRACTOR_BUTTON).click()

    @testit.step('Select contractor {contractor} in form object contract KIP')
    def set_contractor(self, contractor: str):
        time.sleep(2)
        keyboard = Controller()
        self._custom_select_method(locator=self._LOCATOR_CONTRACTOR, text=contractor)
        time.sleep(1)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    @testit.step('Set frame {frame} }in form object contract KIP')
    def set_frame(self, frame: int):
        time.sleep(2)
        self.find_element(locator=self._LOCATOR_FRAME).clear()
        self.find_element(locator=self._LOCATOR_FRAME).send_keys(frame)

    @testit.step('Click save contractor in form object contract KIP')
    def push_save_contractor_button(self):
        self.find_element(locator=self._LOCATOR_SUBMIT_BUTTON).click()

    @testit.step('Set discount {discount} }in form object contract KIP')
    def set_discount(self, discount):
        self.find_element(locator=self._LOCATOR_DISCOUNT).clear()
        self.find_element(locator=self._LOCATOR_DISCOUNT).send_keys(discount)

    @testit.step('Click save button in object contract KIP')
    def push_save_order_button(self):
        self.find_element(locator=self._LOCATOR_SAVE_ORDER_BUTTON).click()

    @testit.step('Add contractor, discount and frame in object contract KIP')
    def add_contractor(self, discount: int, contractor: str, frame: int):
        self.check_loader()
        self.push_change_contractor_button()
        self.set_contractor(contractor)
        self.set_frame(frame)
        self.push_save_contractor_button()
        self.check_loader()
        self.set_discount(discount)
        self.push_save_order_button()
