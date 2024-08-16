from locator import Locator, Input, Select
from page import Page
import time
import testit


class FormB2CObjectOrder(Page):
    name = 'Объекты заказа КИП'
    path = 'b2c/group_orders'

    _ORDER_ID = '.form-group.mb-0 .js--load-tab.js--new-tab'
    _LOCATOR_CHANGE_CONTRACTOR_BUTTON = '//button[@form[contains(., "form-change-client")]]'
    _LOCATOR_CONTRACTOR = '//div[@title = "Подрядчик"]'
    _LOCATOR_FRAME = '//input[@id[contains(., "contractorCode")]]'
    _LOCATOR_SUBMIT_BUTTON = '//div[@class = "modal-footer"]/ancestor::div[2]//button[text() = "Сохранить"]'
    _LOCATOR_DISCOUNT = '//input[@name= "discount"]'
    _LOCATOR_SAVE_ORDER_BUTTON = '//div[@class= "row mb-10"]//button[@type = "submit"]'

    @classmethod
    @testit.step('Open form object contract KIP by order {order}')
    def open_form(cls, order_id: int):
        cls.open_with_path(f'/{order_id}')

    @classmethod
    @testit.step('Get order id in form object contract KIP')
    def get_custom_order_order_id(cls) -> int:
        return int(str(Locator(cls._ORDER_ID).text).strip())

    @classmethod
    @testit.step('Custom select form object contract KIP by {locator} and text {text}')
    def _custom_select_method(cls, locator, text):
        Locator(locator).click()
        Input(f'{locator}//input[@type="text"]').input(text)

    @classmethod
    @testit.step('Click change contractor in form object contract KIP')
    def push_change_contractor_button(cls):
        Locator(cls._LOCATOR_CHANGE_CONTRACTOR_BUTTON).click()

    @classmethod
    @testit.step('Select contractor {contractor} in form object contract KIP')
    def set_contractor(cls, contractor: str):
        cls._custom_select_method(cls._LOCATOR_CONTRACTOR, text=contractor)

    @classmethod
    @testit.step('Set frame {frame} }in form object contract KIP')
    def set_frame(cls, frame: int):
        Input(cls._LOCATOR_FRAME).input(str(frame))

    @classmethod
    @testit.step('Click save contractor in form object contract KIP')
    def push_save_contractor_button(cls):
        Locator(cls._LOCATOR_SUBMIT_BUTTON).click()

    @classmethod
    @testit.step('Set discount {discount} }in form object contract KIP')
    def set_discount(cls, discount):
        Input(cls._LOCATOR_DISCOUNT).input(discount)

    @classmethod
    @testit.step('Click save button in object contract KIP')
    def push_save_order_button(cls):
        Locator(cls._LOCATOR_SAVE_ORDER_BUTTON).click()

    @classmethod
    @testit.step('Add contractor, discount and frame in object contract KIP')
    def add_contractor(cls, discount: int, contractor: str, frame: int):
        cls.push_change_contractor_button()
        cls.set_contractor(contractor)
        cls.set_frame(frame)
        cls.push_save_contractor_button()
        cls.set_discount(discount)
        cls.push_save_order_button()
