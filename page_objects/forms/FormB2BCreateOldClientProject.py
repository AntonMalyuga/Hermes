from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import testit


class FormB2BCreateOldClientProject:
    name = 'Создать старый клиентский проект'
    path = 'client/showkpform'

    _LOCATOR_INPUT_TYPE_PRE_SALE = (By.XPATH, '//input[@id="PARAMS[preSaleCB]"]')
    _LOCATOR_INPUT_CLIENT_NAME = (By.XPATH, '//input[@name="CUSTOMER[CUSTOM_NAME]"]')
    _LOCATOR_INPUT_CLIENT_INN = (By.XPATH, '//input[@id="CUSTOMER[CUSTOM_INN]"]')
    _LOCATOR_INPUT_CLIENT_KPP = (By.XPATH, '//input[@id="CUSTOMER[CUSTOM_OKONH]"]')

    _LOCATOR_BTN_UPDATE_CLIENT = (By.XPATH, '//button[@name="FORM_PREFILL" and @value="CLIENT"]')
    _LOCATOR_BTN_INSERT_EXIST_CLIENT = (By.XPATH, '//button[@name="FORM_PREFILL" and contains(@value, "ADD_CLIENT")]')

    _LOCATOR_INPUT_CONTACT_NAME = (By.XPATH, '//input[@name="CUSTOMER[CUSTOM_CONTACT_PERSON]"]')
    _LOCATOR_INPUT_CONTACT_TELEPHONE_NUMBER = (By.XPATH, '//input[@name="CUSTOMER[CUSTOM_CONTACT_PHONE]"]')
    _LOCATOR_INPUT_CONTACT_EMAIL = (By.XPATH, '//input[@name="CUSTOMER[CUSTOM_CONTACT_EMAIL]"]')

    _LOCATOR_TABLE_CREATED_CLIENTS_NAME = (By.XPATH, '//div[@class="scrollable-div"]//span[@class="col-xs-8"]')
    _LOCATOR_TABLE_CREATED_CLIENTS_INN = (By.XPATH, '//div[@class="scrollable-div"]//span[@class="col-xs-1"][2]')
    _LOCATOR_TABLE_CREATED_CLIENTS_KPP = (By.XPATH, '//div[@class="scrollable-div"]//span[@class="col-xs-1"][3]')

    _LOCATOR_INPUT_NEW_PROJECT_NAME = (By.XPATH, '//input[@data-event-name="CRM_PROMOTION_ID.1"]')

    _LOCATOR_INPUT_NAME_MANAGER_KB = (By.XPATH, '//input[@id="CONTRACT[CRM_SUBCHANNEL]"]')
    _LOCATOR_INPUT_TELEPHONE_MANAGER_KB = (By.XPATH, '//input[@id="CONTRACT[MANAGER_KB_PHONE]"]')
    _LOCATOR_INPUT_EMAIL_MANAGER_KB = (By.XPATH, '//input[@id="CONTRACT[MANAGER_KB_EMAIL]"]')

    _LOCATOR_SELECT_MACRO_SEGMENT = (By.XPATH, '//select[@name="CONTRACT[CRM_PROMOTION_TYPE]"]')
    _LOCATOR_SELECT_SEGMENT = (By.XPATH, '//input[contains(@id, "CONTRACT[CRM_PROMOTION_SEGMENT]")]')

    _LOCATOR_INPUT_CHANNEL_SALES = (By.XPATH, '//input[contains(@id, "CONTRACT[CRM_CHANNEL_ID]")]')
    _LOCATOR_INPUT_CUSTOMER_ORGANIZATION_TERM = (By.XPATH, '//input[@id="CONTRACT[CUSTOMER_ORGANIZATION_TERM]"]')

    _LOCATOR_SELECT_CLIENTS_BY_ADDRESS = (By.XPATH, '//select[contains(@name, "ADDR_CLIENTS")]')

    _LOCATOR_SELECT_ADDRESS_LVL_ONE = (By.XPATH, '//select[@id="ADDRESSES[0][ATDOBJECT][0]"]')
    _LOCATOR_SELECT_ADDRESS_LVL_TWO = (By.XPATH, '//select[@id="ADDRESSES[0][ATDOBJECT][1]"]')
    _LOCATOR_SELECT_STREET = (By.XPATH, '//select[@id="ADDRESSES[0][ATDSTREET]"]')
    _LOCATOR_SELECT_HOUSE = (By.XPATH, '//select[@id="ADDRESSES[0][ATDHOUSE]"]')

    _LOCATOR_DIV_GROUP_PAYBACK = (By.XPATH, '//h6[@data-event-name="Параметры, влияющие на окупаемость"]')
    _LOCATOR_SELECT_SCALE_SERVICE_SPEED = (By.XPATH, '//select[@name="SERVICES[0][SRV_CMS_ServiceSpeed_SCALE]"]')
    _LOCATOR_INPUT_SERVICE_SPEED = (By.XPATH, '//input[@id="SERVICES[0][SRV_CMS_ServiceSpeed]"]')

    _LOCATOR_DIV_GROUP_PARAMETERS = (By.XPATH, '//h6[@data-event-name="Параметры"]')
    _LOCATOR_INPUT_SRV_FEE_INSTALL = (By.XPATH, '//input[@id="SERVICES[0][SRV_FEE_INSTALL]"]')
    _LOCATOR_INPUT_SERVICE_QTY = (By.XPATH, '//input[@id="SERVICES[0][SERVICE_QTY]"]')
    _LOCATOR_INPUT_SERVICE_FEE_MONTHLY = (By.XPATH, '//input[@id="SERVICES[0][SRV_FEE_MONTHLY]"]')

    _LOCATOR_STRONG_CREATED_ORDERS = (By.XPATH, '//div[@class="alert alert-success alert-dismissable"]//strong')

    _LOCATOR_BUTTON_SUBMIT_FORM = (By.XPATH, '//button[@name="FORM_PREFILL" and @value="SUBMIT"]')

    def _custom_select_method(self, locator, text):
        with testit.step(f'Выбрать значение "{text}" по локатору "{locator}" в форме создания проекта B2B'):
            locator_input = self.find_element((By.XPATH, f'{locator[1]}//following::div[1]//input[@type="text"]'))

            self.find_element((By.XPATH, f'{locator[1]}/following::div[1]')).click()
            time.sleep(1)
            locator_input.send_keys(text)
            time.sleep(1)
            self.find_element((By.XPATH, f'{locator[1]}/following::div[1]//span[1]/span')).click()

    def set_teo_start_stage(self):
        with testit.step('Устанавливаю точку создания на ТЭО'):
            self.find_element(self._LOCATOR_INPUT_TYPE_PRE_SALE).click()

    def set_client_name(self, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            self.find_element(self._LOCATOR_INPUT_CLIENT_NAME).send_keys(name)

    def set_client_inn(self, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            self.find_element(self._LOCATOR_INPUT_CLIENT_INN).send_keys(name)

    def set_client_kpp(self, name: str):
        with testit.step(f'Устанавливаю имя клиента: "{name}"'):
            self.find_element(self._LOCATOR_INPUT_CLIENT_KPP).send_keys(name)

    def update_client(self):
        with testit.step(f'Нажать кнопку "Обновить клиента"'):
            self.find_element(self._LOCATOR_BTN_UPDATE_CLIENT).click()

    def insert_client(self, index_client: int):
        with testit.step(f'Добавить клиента по индексу {index_client}'):
            self.find_elements(self._LOCATOR_BTN_INSERT_EXIST_CLIENT)[index_client].click()

    def set_contact_name(self, contact_name: str):
        with testit.step(f'Установить имя контакта: "{contact_name}"'):
            self.find_element(self._LOCATOR_INPUT_CONTACT_NAME).send_keys(contact_name)

    def set_contact_telephone_number(self, telephone_number: str):
        with testit.step(f'Установить телефонный номер контакта: "{telephone_number}"'):
            self.find_element(self._LOCATOR_INPUT_CONTACT_TELEPHONE_NUMBER).send_keys(telephone_number)

    def set_contact_email(self, email: str):
        with testit.step(f'Установить почтовый адрес контакта: "{email}"'):
            self.find_element(self._LOCATOR_INPUT_CONTACT_EMAIL).send_keys(email)

    def get_info_created_clients(self) -> list:
        clients_data = []
        clients_name = self.find_elements(self._LOCATOR_TABLE_CREATED_CLIENTS_NAME)

        for i in range(len(clients_name)):
            client = {
                'name': self.find_elements(self._LOCATOR_TABLE_CREATED_CLIENTS_NAME)[i].text,
                'inn': self.find_elements(self._LOCATOR_TABLE_CREATED_CLIENTS_INN)[i].text,
                'kpp': self.find_elements(self._LOCATOR_TABLE_CREATED_CLIENTS_KPP)[i].text
            }
            clients_data.append(client)

        return clients_data

    def set_new_project_name(self, project_name: str):
        with testit.step(f'Установить новое наименование проекта: "{project_name}"'):
            self.find_element(self._LOCATOR_INPUT_NEW_PROJECT_NAME).send_keys(
                f'{project_name} уникальный {time.time()}')

    def set_name_manager_kb(self, name_manager_kb: str):
        with testit.step(f'Установить имя менеджера КБ: "{name_manager_kb}"'):
            self.find_element(self._LOCATOR_INPUT_NAME_MANAGER_KB).send_keys(name_manager_kb)

    def set_telephone_manager_kb(self, telephone_number_manager_kb: str):
        with testit.step(f'Установить телефон менеджера КБ: "{telephone_number_manager_kb}"'):
            self.find_element(self._LOCATOR_INPUT_TELEPHONE_MANAGER_KB).send_keys(telephone_number_manager_kb)

    def set_email_manager_kb(self, email_manager_kb: str):
        with testit.step(f'Установить почтоный адрес менеджера КБ: "{email_manager_kb}"'):
            self.find_element(self._LOCATOR_INPUT_EMAIL_MANAGER_KB).send_keys(email_manager_kb)

    def set_macro_segment(self, macro_segment: str):
        with testit.step(f'Установить макросегмент: "{macro_segment}"'):
            self._custom_select_method(self._LOCATOR_SELECT_MACRO_SEGMENT, macro_segment)

    def set_segment(self, segment: str):
        with testit.step(f'Установить сегмент: "{segment}"'):
            self._custom_select_method(self._LOCATOR_SELECT_SEGMENT, segment)

    def set_chanel_sales(self, chanel_sales: str):
        with testit.step(f'Установить канал продаж: "{chanel_sales}"'):
            self._custom_select_method(self._LOCATOR_INPUT_CHANNEL_SALES, chanel_sales)

    def set_organization_term(self, data: str):
        with testit.step(f'Установить клиентский срок организации: "{data}"'):
            self.find_element(self._LOCATOR_INPUT_CUSTOMER_ORGANIZATION_TERM).send_keys(data)

    def set_location_lvl_one(self, location_name: str):
        with testit.step(
                f'Установить адрес уровня 1: "{location_name}" в форме создаиня старого клиентского проекта'):
            self._custom_select_method(locator=self._LOCATOR_SELECT_ADDRESS_LVL_ONE, text=location_name)

    def set_location_lvl_two(self, location_name: str):
        with testit.step(
                f'Установить адрес уровня 2: "{location_name}" в форме создаиня старого клиентского проекта'):
            self._custom_select_method(locator=self._LOCATOR_SELECT_ADDRESS_LVL_TWO, text=location_name)

    def set_street(self, street_name: str):
        with testit.step(
                f'Установить улицу: "{street_name}" в форме создаиня старого клиентского проекта'):
            self._custom_select_method(locator=self._LOCATOR_SELECT_STREET, text=street_name)

    def set_house(self, house_name: str):
        with testit.step(
                f'Установить дом: "{house_name}" в форме создаиня старого клиентского проекта'):
            self._custom_select_method(locator=self._LOCATOR_SELECT_HOUSE, text=house_name)

    def set_client_on_addresses(self):
        with testit.step(f'Установить выбранного клиента на адреса'):
            addresses = self.find_elements(self._LOCATOR_SELECT_CLIENTS_BY_ADDRESS)
            for address in addresses:
                Select(address).select_by_index(1)

    def click_group_parameters(self):
        with testit.step(f'Кликнуть на группу "Параметры"'):
            self.find_element(self._LOCATOR_DIV_GROUP_PARAMETERS).click()

    def set_scale_servie_speed(self, scale_service: str):
        with testit.step(f'Установить масштаб скорости канала: {scale_service}'):
            self._custom_select_method(self._LOCATOR_SELECT_SCALE_SERVICE_SPEED, scale_service)

    def set_service_speed(self, speed: int):
        with testit.step(f'Установить скорость канала: {speed}'):
            element = self.find_element(self._LOCATOR_INPUT_SERVICE_SPEED)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(speed)

    def set_srv_fee_install(self, ruble: int):
        with testit.step(f'Установить единовременную сумму оплаты: {ruble}'):
            element = self.find_element(self._LOCATOR_INPUT_SRV_FEE_INSTALL)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(ruble)

    def click_group_payback(self):
        with testit.step(f'Кликнуть на группу "Параметры, влияющие на окупаемость"'):
            self.find_element(self._LOCATOR_DIV_GROUP_PAYBACK).click()

    def set_service_qty(self, cnt: int):
        with testit.step(f'Установить количество приростаные: {cnt}'):
            element = self.find_element(self._LOCATOR_INPUT_SERVICE_QTY)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(cnt)

    def set_fee_monthly(self, ruble: int):
        with testit.step(f'Установить ежемесячную сумму оплаты: {ruble}'):
            element = self.find_element(self._LOCATOR_INPUT_SERVICE_FEE_MONTHLY)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(ruble)

    def open_created_client_order(self) -> int:
        self.find_elements(self._LOCATOR_STRONG_CREATED_ORDERS)[0].click()

    def get_created_client_order(self) -> int:
        return int(self.find_elements(self._LOCATOR_STRONG_CREATED_ORDERS)[0].text)

    def open_created_client_project_order(self) -> int:
        self.find_elements(self._LOCATOR_STRONG_CREATED_ORDERS)[1].click()

    def get_created_client_project_order(self) -> int:
        return int(self.find_elements(self._LOCATOR_STRONG_CREATED_ORDERS)[1].text)

    def submit(self):
        with testit.step('Нажимаю на кнопку "Отправить на проработку ТР"'):
            self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    @testit.step('Заполнить параметры для создания проекта B2B на ТЭО')
    def create_project_on_teo(self):
        self.set_teo_start_stage()
        time.sleep(2)
        self.check_loader()
        time.sleep(2)
        self.set_client_name('ТЕСТ-ГЕРМЕС')
        self.set_client_inn('006165139943')
        self.set_client_kpp('616501001')
        time.sleep(1)
        self.update_client()
        self.check_loader()
        self.insert_client(0)
        time.sleep(7)
        self.set_contact_name('Малюга А.С.')
        self.set_contact_telephone_number('8(999)999-99-99')
        self.set_contact_email('test@test.test')
        self.set_new_project_name('Проект проект уникальщина')
        self.set_name_manager_kb('Малюга А.С.')
        self.set_telephone_manager_kb('8(999)999-99-99')
        self.set_email_manager_kb('testkb@test.test')
        self.set_macro_segment('B2B')
        time.sleep(2)
        self.set_segment('Клиенты федерального уровня (ККФУ)')
        time.sleep(2)
        self.set_chanel_sales('Активный канал/3К АП (хантеры)')
        time.sleep(2)
        self.set_organization_term('24.05.2024')
        self.set_location_lvl_one('Саратовская область')
        time.sleep(1)
        self.set_location_lvl_two('Саратов город')
        time.sleep(3)
        self.set_street('ул Авиастроителей')
        time.sleep(5)
        self.set_house('д. 3')
        self.set_client_on_addresses()
        self.click_group_payback()
        self.set_srv_fee_install(1000)
        self.set_service_qty(2)
        self.set_fee_monthly(300)
        self.click_group_parameters()
        self.set_scale_servie_speed('кбит/с')
        self.set_service_speed(250)
        self.submit()
