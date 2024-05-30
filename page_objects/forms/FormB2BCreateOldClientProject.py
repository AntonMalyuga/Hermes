from page import Page
from locator import Locator, Input, CheckBox, Select
from VO.FormB2BCreateOldProject import Project
import time
import testit


class FormB2BCreateOldClientProject(Page):
    name = 'Создать старый клиентский проект'
    path = 'client/showkpform'

    _LOCATOR_INPUT_TYPE_PRE_SALE = '//input[@id="PARAMS[preSaleCB]"]'
    _LOCATOR_INPUT_CLIENT_NAME = '//input[@name="CUSTOMER[CUSTOM_NAME]"]'
    _LOCATOR_INPUT_CLIENT_INN = '//input[@id="CUSTOMER[CUSTOM_INN]"]'
    _LOCATOR_INPUT_CLIENT_KPP = '//input[@id="CUSTOMER[CUSTOM_OKONH]"]'

    _LOCATOR_BTN_UPDATE_CLIENT = '//button[@name="FORM_PREFILL" and @value="CLIENT"]'
    _LOCATOR_BTN_INSERT_EXIST_CLIENT = '//button[@name="FORM_PREFILL" and contains(@value, "ADD_CLIENT")]'
    _LOCATOR_H5_CHECK_INSERT_CLIENT = '//h5[text()="Выбранные клиенты"]'

    _LOCATOR_INPUT_CONTACT_NAME = '//input[@name="CUSTOMER[CUSTOM_CONTACT_PERSON]"]'
    _LOCATOR_INPUT_CONTACT_TELEPHONE_NUMBER = '//input[@name="CUSTOMER[CUSTOM_CONTACT_PHONE]"]'
    _LOCATOR_INPUT_CONTACT_EMAIL = '//input[@name="CUSTOMER[CUSTOM_CONTACT_EMAIL]"]'

    _LOCATOR_TABLE_CREATED_CLIENTS_NAME = '//div[@class="scrollable-div"]//span[@class="col-xs-8"]'
    _LOCATOR_TABLE_CREATED_CLIENTS_INN = '//div[@class="scrollable-div"]//span[@class="col-xs-1"][2]'
    _LOCATOR_TABLE_CREATED_CLIENTS_KPP = '//div[@class="scrollable-div"]//span[@class="col-xs-1"][3]'

    _LOCATOR_INPUT_NEW_PROJECT_NAME = '//input[@data-event-name="CRM_PROMOTION_ID.1"]'

    _LOCATOR_INPUT_NAME_MANAGER_KB = '//input[@id="CONTRACT[CRM_SUBCHANNEL]"]'
    _LOCATOR_INPUT_TELEPHONE_MANAGER_KB = '//input[@id="CONTRACT[MANAGER_KB_PHONE]"]'
    _LOCATOR_INPUT_EMAIL_MANAGER_KB = '//input[@id="CONTRACT[MANAGER_KB_EMAIL]"]'

    _LOCATOR_SELECT_MACRO_SEGMENT = '//select[@name="CONTRACT[CRM_PROMOTION_TYPE]"]'
    _LOCATOR_SELECT_SEGMENT = '//input[contains(@id, "CONTRACT[CRM_PROMOTION_SEGMENT]")]'

    _LOCATOR_INPUT_CHANNEL_SALES = '//input[contains(@id, "CONTRACT[CRM_CHANNEL_ID]")]'
    _LOCATOR_INPUT_CUSTOMER_ORGANIZATION_TERM = '//input[@id="CONTRACT[CUSTOMER_ORGANIZATION_TERM]"]'

    _LOCATOR_SELECT_CLIENTS_BY_ADDRESS = '//select[contains(@name, "ADDR_CLIENTS")]'

    _LOCATOR_SELECT_ADDRESS_LVL_ONE = '//select[@id="ADDRESSES[0][ATDOBJECT][0]"]'
    _LOCATOR_SELECT_ADDRESS_LVL_TWO = '//select[@id="ADDRESSES[0][ATDOBJECT][1]"]'
    _LOCATOR_SELECT_ADDRESS_LVL_THREE = '//select[@id="ADDRESSES[0][ATDOBJECT][2]"]'
    _LOCATOR_SELECT_STREET = '//select[@id="ADDRESSES[0][ATDSTREET]"]'
    _LOCATOR_SELECT_HOUSE = '//select[@id="ADDRESSES[0][ATDHOUSE]"]'

    _LOCATOR_CHECKBOX_TVP = '//input[@name="ADDRESSES[0][CRMWorkingKind]"]'

    _LOCATOR_DIV_GROUP_PAYBACK = '//h6[@data-event-name="Параметры, влияющие на окупаемость"]'
    _LOCATOR_SELECT_SCALE_SERVICE_SPEED = '//select[@name="SERVICES[0][SRV_CMS_ServiceSpeed_SCALE]"]'
    _LOCATOR_INPUT_SERVICE_SPEED = '//input[@id="SERVICES[0][SRV_CMS_ServiceSpeed]"]'

    _LOCATOR_DIV_GROUP_PARAMETERS = '//h6[@data-event-name="Параметры"]'
    _LOCATOR_INPUT_SRV_FEE_INSTALL = '//input[@id="SERVICES[0][SRV_FEE_INSTALL]"]'
    _LOCATOR_INPUT_SERVICE_QTY = '//input[@id="SERVICES[0][SERVICE_QTY]"]'
    _LOCATOR_INPUT_SERVICE_FEE_MONTHLY = '//input[@id="SERVICES[0][SRV_FEE_MONTHLY]"]'

    _LOCATOR_STRONG_CREATED_ORDER_KZ = '//span[contains(text(), "Клиентская заявка")]//a'
    _LOCATOR_STRONG_CREATED_ORDER_KP = '//span[contains(text(), "Клиентский проект")]//a'

    _LOCATOR_BUTTON_SUBMIT_FORM = '//button[@name="FORM_PREFILL" and @value="SUBMIT"]'

    @classmethod
    def wait_reload_page(cls, time_wait: int = 2):
        Locator(cls._LOCATOR_RELOAD_PAGE).wait_attached()
        time.sleep(time_wait)

    @classmethod
    def set_teo_start_stage(cls):
        with testit.step('Устанавливаю точку создания на ТЭО'):
            CheckBox(cls._LOCATOR_INPUT_TYPE_PRE_SALE).unchecked()

    @classmethod
    def set_client_name(cls, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            Input(cls._LOCATOR_INPUT_CLIENT_NAME).input(name)

    @classmethod
    def set_client_inn(cls, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            Input(cls._LOCATOR_INPUT_CLIENT_INN).input(name)

    @classmethod
    def set_client_kpp(cls, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            Input(cls._LOCATOR_INPUT_CLIENT_KPP).input(name)

    @classmethod
    def update_client(cls):
        with testit.step(f'Нажать кнопку "Обновить клиента"'):
            Locator(cls._LOCATOR_BTN_UPDATE_CLIENT).click()

    @classmethod
    def get_find_client(cls, inn: str, kpp: str, client_name: str) -> Locator:
        return Locator(
            f'//div[@class="row scrollable-row" and .//span[text()="{inn}"] and .//span[text()="{kpp}"] and .//span[text()="{client_name}"]]//button')

    @classmethod
    def set_find_client(cls, inn: str, kpp: str, client_name: str):
        with testit.step(f'Добавить первого найденного клиента'):
            cls.get_find_client(inn, kpp, client_name).click()

    @classmethod
    def check_insert_client(cls):
        with testit.step('Проверить добавление клиента'):
            Locator(cls._LOCATOR_H5_CHECK_INSERT_CLIENT).is_on_page()

    @classmethod
    def set_contact_name(cls, contact_name: str):
        with testit.step(f'Установить имя контакта: "{contact_name}"'):
            Input(cls._LOCATOR_INPUT_CONTACT_NAME).input(contact_name)

    @classmethod
    def set_contact_telephone_number(cls, telephone_number: str):
        with testit.step(f'Установить телефонный номер контакта: "{telephone_number}"'):
            Input(cls._LOCATOR_INPUT_CONTACT_TELEPHONE_NUMBER).input(telephone_number)

    @classmethod
    def set_contact_email(cls, email: str):
        with testit.step(f'Установить почтовый адрес контакта: "{email}"'):
            Input(cls._LOCATOR_INPUT_CONTACT_EMAIL).input(email)

    @classmethod
    def set_new_project_name(cls, project_name: str):
        with testit.step(f'Установить новое наименование проекта: "{project_name}"'):
            Input(cls._LOCATOR_INPUT_NEW_PROJECT_NAME).input(f'{project_name} уникальный {time.time()}')

    @classmethod
    def set_name_manager_kb(cls, name_manager_kb: str):
        with testit.step(f'Установить имя менеджера КБ: "{name_manager_kb}"'):
            Input(cls._LOCATOR_INPUT_NAME_MANAGER_KB).input(name_manager_kb)

    @classmethod
    def set_telephone_manager_kb(cls, telephone_number_manager_kb: str):
        with testit.step(f'Установить телефон менеджера КБ: "{telephone_number_manager_kb}"'):
            Input(cls._LOCATOR_INPUT_TELEPHONE_MANAGER_KB).input(telephone_number_manager_kb)

    @classmethod
    def set_email_manager_kb(cls, email_manager_kb: str):
        with testit.step(f'Установить почтоный адрес менеджера КБ: "{email_manager_kb}"'):
            Input(cls._LOCATOR_INPUT_EMAIL_MANAGER_KB).input(email_manager_kb)

    @classmethod
    def set_macro_segment(cls, macro_segment: str):
        with testit.step(f'Установить макросегмент: "{macro_segment}"'):
            Select(cls._LOCATOR_SELECT_MACRO_SEGMENT).ajax_option(macro_segment)

    @classmethod
    def set_segment(cls, segment: str):
        with testit.step(f'Установить сегмент: "{segment}"'):
            Select(cls._LOCATOR_SELECT_SEGMENT).ajax_option(segment)

    @classmethod
    def set_chanel_sales(cls, chanel_sales: str):
        with testit.step(f'Установить канал продаж: "{chanel_sales}"'):
            Select(cls._LOCATOR_INPUT_CHANNEL_SALES).ajax_option(chanel_sales)

    @classmethod
    def set_organization_term(cls, data: str):
        with testit.step(f'Установить клиентский срок организации: "{data}"'):
            Input(cls._LOCATOR_INPUT_CUSTOMER_ORGANIZATION_TERM).input(data)

    @classmethod
    def set_location_lvl_one(cls, location_name: str):
        with testit.step(f'Установить адрес уровня 1: "{location_name}" в форме создаиня старого клиентского проекта'):
            Select(cls._LOCATOR_SELECT_ADDRESS_LVL_ONE).ajax_option(location_name)

    @classmethod
    def set_location_lvl_two(cls, location_name: str):
        with testit.step(f'Установить адрес уровня 2: "{location_name}" в форме создаиня старого клиентского проекта'):
            Select(cls._LOCATOR_SELECT_ADDRESS_LVL_TWO).ajax_option(location_name)

    @classmethod
    def check_location_lvl_three(cls):
        Locator(cls._LOCATOR_SELECT_ADDRESS_LVL_THREE).is_on_page()

    @classmethod
    def set_street(cls, street_name: str):
        with testit.step(f'Установить улицу: "{street_name}" в форме создаиня старого клиентского проекта'):
            Select(cls._LOCATOR_SELECT_STREET).ajax_option(street_name)

    @classmethod
    def set_house(cls, house_name: str):
        with testit.step(f'Установить дом: "{house_name}" в форме создаиня старого клиентского проекта'):
            Select(cls._LOCATOR_SELECT_HOUSE).ajax_option(house_name)

    @classmethod
    def set_client_on_addresses_by_index(cls, index: int):
        with testit.step(f'Установить выбранного клиента на адреса'):
            Select(cls._LOCATOR_SELECT_CLIENTS_BY_ADDRESS).index(index)

    @classmethod
    def set_tvp(cls):
        CheckBox(cls._LOCATOR_CHECKBOX_TVP).checked()

    @classmethod
    def click_group_parameters(cls):
        with testit.step(f'Кликнуть на группу "Параметры"'):
            Locator(cls._LOCATOR_DIV_GROUP_PARAMETERS).click()

    @classmethod
    def set_scale_servie_speed(cls, scale_service: str):
        with testit.step(f'Установить масштаб скорости канала: {scale_service}'):
            Select(cls._LOCATOR_SELECT_SCALE_SERVICE_SPEED).ajax_option(scale_service)

    @classmethod
    def set_service_speed(cls, speed: int):
        with testit.step(f'Установить скорость канала: {speed}'):
            Input(cls._LOCATOR_INPUT_SERVICE_SPEED).input(str(speed))

    @classmethod
    def set_srv_fee_install(cls, ruble: int):
        with testit.step(f'Установить единовременную сумму оплаты: {ruble}'):
            Input(cls._LOCATOR_INPUT_SRV_FEE_INSTALL).input(str(ruble))

    @classmethod
    def click_group_payback(cls):
        with testit.step(f'Кликнуть на группу "Параметры, влияющие на окупаемость"'):
            Locator(cls._LOCATOR_DIV_GROUP_PAYBACK).click()

    @classmethod
    def set_service_qty(self, cnt: int):
        with testit.step(f'Установить количество приростаные: {cnt}'):
            Input(self._LOCATOR_INPUT_SERVICE_QTY).input(str(cnt))

    @classmethod
    def set_fee_monthly(cls, ruble: int):
        with testit.step(f'Установить ежемесячную сумму оплаты: {ruble}'):
            Input(cls._LOCATOR_INPUT_SERVICE_FEE_MONTHLY).input(str(ruble))

    @classmethod
    def open_created_client_order(cls):
        return Locator(cls._LOCATOR_STRONG_CREATED_ORDER_KZ).click()

    @classmethod
    def get_created_client_order(cls) -> int:
        return int(Locator(cls._LOCATOR_STRONG_CREATED_ORDER_KZ).text)

    @classmethod
    def open_created_client_project_order(cls):
        Locator(cls._LOCATOR_STRONG_CREATED_ORDER_KP).click()

    @classmethod
    def get_created_client_project_order(cls) -> int:
        return int(Locator(cls._LOCATOR_STRONG_CREATED_ORDER_KP).text)

    @classmethod
    def submit(cls):
        with testit.step('Нажимаю на кнопку "Отправить на проработку ТР"'):
            Locator(cls._LOCATOR_BUTTON_SUBMIT_FORM).click()

    @classmethod
    @testit.step('Заполнить параметры для создания проекта B2B')
    def create_project(cls, project: Project):

        if project.is_teo:
            cls.set_teo_start_stage()
        time.sleep(6)

        cls.set_client_name(project.client_name)
        cls.set_client_inn(project.client_inn)
        cls.set_client_kpp(project.client_kpp)
        cls.update_client()
        cls.set_find_client(inn=project.client_inn, kpp=project.client_kpp, client_name=project.client_name)
        cls.check_insert_client()
        cls.set_contact_name(project.contact_name)
        cls.set_contact_telephone_number(project.contact_telephone_number)
        cls.set_contact_email(project.contact_email)
        cls.set_new_project_name(project.new_project_name)
        cls.set_name_manager_kb(project.manager_kb_name)
        cls.set_telephone_manager_kb(project.manager_kb_telephone_number)
        cls.set_email_manager_kb(project.manager_kb_email)
        cls.set_macro_segment(project.manager_kb_macro_segment)
        cls.set_segment(project.manager_kb_segment)
        cls.set_chanel_sales(project.chanel_sales)
        cls.set_organization_term(project.organization_term)
        cls.set_location_lvl_one(project.location_lvl_one)
        cls.set_location_lvl_two(project.location_lvl_two)
        cls.check_location_lvl_three()
        cls.set_street(project.street)
        if project.is_tvp:
            cls.set_tvp()
        time.sleep(2)
        cls.set_house(project.house)
        cls.set_client_on_addresses_by_index(1)
        cls.click_group_payback()
        cls.set_srv_fee_install(project.srv_fee_install)
        cls.set_service_qty(project.service_qty)
        cls.set_fee_monthly(project.fee_monthly)
        cls.click_group_parameters()
        cls.set_scale_servie_speed(project.scale_servie_speed)
        cls.set_service_speed(project.service_speed)
        cls.submit()
