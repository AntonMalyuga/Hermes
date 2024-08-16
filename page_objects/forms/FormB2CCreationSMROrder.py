from pynput.keyboard import Key, Controller
from locator import Locator, Input, Select
from page import Page
import time
import testit
from api.Sys import SysAPI


class FormB2CCreationSMROrder(Page):
    name = 'Создать заявку СМР'
    path = 'client/createb2c'

    _LOCATOR_BUILDING_TYPE = '//select[@class= "form-control input-sm input-reload-onchange suggest__hidden-accessible"]'
    _LOCATOR_BUILDING_FLOORS = '//input[@id[contains(., "ADDRESSPARAMS[MAX_ETAZH]")]]'
    _LOCATOR_BUILDING_ENTRANCES = '//input[@id[contains(., "ADDRESSPARAMS[CNT_PODJEZD]")]]'
    _LOCATOR_BUILDING_FLAT_AT_FLOOR = '//input[@id[contains(., "ADDRESSPARAMS[FLAT_AT_FLOOR]")]]'
    _LOCATOR_BUILDING_DH_COUNTER = '//input[@id[contains(., "ADDRESSPARAMS[COUNT_FLATS]")]]'
    _LOCATOR_BUILDING_COMMERCE_PLAN = '//input[@id[contains(., "ADDRESSPARAMS[PP_DRS]")]]'
    _LOCATOR_BUILDING_AP_YEAR = '//div[@class = "form-group  has-warning"]//div[@class = "suggest form-control input-sm js--matomo-log-focus-event"]'

    _LOCATOR_LOCATION = '//div[@class = "suggest form-control select-service-address input-sm"]'
    _LOCATOR_STREET = '//label[@for= "ADDRESS[ATDSTREET]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]'

    _LOCATOR_HOUSE = '//label[@for= "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//div[@class = "suggest form-control select-service-address input-sm"]'

    _LOCATOR_CLIENT = '//div[@style = "display: flex"]//div[@class= "suggest form-control input-sm js--matomo-log-focus-event"]'
    _LOCATOR_OBJECT_TYPE = '//div[@class = "form-group has-warning"]//div[@class = "suggest form-control select-service-address input-sm"]'
    _LOCATOR_OBJECT_TYPE_DISABLED = '//select[@name = "ADDRESS[CRM_OBJECT_TYPE]"]'
    _LOCATOR_WIFI_CHECKBOX = '//div[@class= "b2c-service-group"]//input[@name= "services[wifi]"]'
    _LOCATOR_CREATE_BUTTON = '//button[@class= "btn btn-primary"]'
    _LOCATOR_ELEMENTS_HOUSES = '//label[@for = "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//span[@class = "name"]'
    _LOCATOR_ELEMENTS_STREETS = '//label[@for = "ADDRESS[ATDSTREET]"]/ancestor::div[2]//span[@class = "name"]'
    _LOCATOR_CREATION_ORDER = '//a[@id="CreateOrderb2C"]'
    _LOCATOR_AREA = '//label[@for= "ADDRESS[ATDOBJECT][1]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]'
    _LOCATOR_VILLAGE = '//label[@for= "ADDRESS[ATDOBJECT][2]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]'
    _LOCATOR_AREA_NAME = '//label[@for= "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]'
    _LOCATOR_MISTAKE = '//h5[@class = "text-danger"]'
    _LOCATOR_CREATING_ORDERS = '//table[@class="table table-condensed table-hover"]//td[text()="B2C"]/following::td[1]/a'

    @classmethod
    @testit.step('Check error add creation order by address in form b2c creation smr')
    def _is_error_add_address_on_creation_order(cls):
        try:
            return len(Locator(cls._LOCATOR_MISTAKE).text) >= 1
        except:
            return False

    @classmethod
    def _delete_creating_orders(cls):
        order_list = Locator(cls._LOCATOR_CREATING_ORDERS).all
        for order in order_list:
            SysAPI().delete_order(int(order.text))

    @classmethod
    def _custom_select_method(cls, locator, text):
        with testit.step(f'Custom select value {text} by {locator} in form b2c creation smr'):
            Input(f'{locator}//input[@type="text"]').input(text)
            Locator(locator).click()

    @classmethod
    def _set_building_type(cls, building_type: str):
        with testit.step(f'Set building type {building_type} in form b2c creation smr'):
            Select(cls._LOCATOR_BUILDING_TYPE).option(building_type)

    @classmethod
    def _set_location(cls, location_name: str):
        time.sleep(2)
        with testit.step(f'Set location {location_name} in form b2c creation smr'):
            cls._custom_select_method(cls._LOCATOR_LOCATION, text=location_name)

    @classmethod
    def _get_streets_name(cls):
        elements = Locator(cls._LOCATOR_ELEMENTS_STREETS).all
        street_names = [element.get_attribute('innerText') for element in elements]
        with testit.step('Get streets names {street_names} in form b2c creation smr'):
            return street_names

    @classmethod
    def _get_house_names(cls):
        elements = Locator(cls._LOCATOR_ELEMENTS_HOUSES).all
        house_names = [element.get_attribute('innerText') for element in elements]
        with testit.step(f'Get houses names {house_names} in form b2c creation smr'):
            return house_names

    @classmethod
    def _set_random_street_and_house(cls):
        streets_name = cls._get_streets_name()
        for street_name in streets_name:
            cls._custom_select_method(cls._LOCATOR_STREET, text=street_name)
            first_police_house = cls._get_police_house()
            if first_police_house:
                cls._set_house(first_police_house)
                if cls._is_error_add_address_on_creation_order():
                    continue
                else:
                    with testit.step(f'Set ramdom street {first_police_house} and house in form b2c creation smr'):
                        break

    @classmethod
    def _get_police_house(cls):
        houses = Locator(cls._LOCATOR_ELEMENTS_HOUSES).all
        for house in houses:
            house_name = house.get_attribute('innerText')
            if str(house_name).find('Милицейские') == -1:
                continue
            else:
                with testit.step(f'Get first police house {house_name} in form b2c creation smr'):
                    return house_name
        return False

    @classmethod
    def _set_house(cls, house_name: str):
        with testit.step(f'Set house {house_name} in form b2c creation smr'):
            cls._custom_select_method(cls._LOCATOR_HOUSE, text=house_name)

    @classmethod
    def _set_client(cls, client_name: str):
        with testit.step(f'Set client {client_name} in form b2c creation smr'):
            keyboard = Controller()
            cls._custom_select_method(cls._LOCATOR_CLIENT, text=client_name)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

    @classmethod
    def _set_object_type(cls, obj_type: str):
        with testit.step('Set object type {obj_type} in form b2c creation smr'):
            cls._custom_select_method(cls._LOCATOR_OBJECT_TYPE, text=obj_type)

    @classmethod
    def _set_building_fields(cls, floors: int, entrances: int, flats: int, dh_counter: int, commerce_plan: int):
        def clear_and_set(locator, value):
            Input(locator).input(value)

        with testit.step(
                f'Set building field {floors}, {entrances}, {flats}, {dh_counter} and {commerce_plan} in form b2c creation smr'):
            clear_and_set(cls._LOCATOR_BUILDING_ENTRANCES, value=entrances)
            clear_and_set(cls._LOCATOR_BUILDING_FLOORS, value=floors)
            clear_and_set(cls._LOCATOR_BUILDING_FLAT_AT_FLOOR, value=flats)
            clear_and_set(cls._LOCATOR_BUILDING_DH_COUNTER, value=dh_counter)
            clear_and_set(cls._LOCATOR_BUILDING_COMMERCE_PLAN, value=commerce_plan)

    @classmethod
    def _set_building_ap_years(cls, ap_year: int):
        with testit.step('Set building ap year {ap_year} in form b2c creation smr'):
            cls._custom_select_method(cls._LOCATOR_BUILDING_AP_YEAR, text=ap_year)

    @classmethod
    def _set_wifi_checkbox(cls):
        with testit.step('Set checkbox wifi in form b2c creation name'):
            Input(cls._LOCATOR_WIFI_CHECKBOX).click()

    @classmethod
    def _create_order(cls):
        with testit.step('Click create order in form b2c creation name'):
            Locator(cls._LOCATOR_CREATE_BUTTON).click()

    @classmethod
    def _set_area(cls, area: str):
        time.sleep(1)
        with testit.step(f'Set area {area} in form b2c creation name'):
            cls._custom_select_method(cls._LOCATOR_AREA, text=area)

    @classmethod
    def _set_village(cls, village: str):
        with testit.step(f'Set village {village} in form b2c creation name'):
            cls._custom_select_method(cls._LOCATOR_VILLAGE, text=village)

    @classmethod
    def _set_area_name(cls, area_name):
        with testit.step(f'Set area name {area_name} in form b2c creation name'):
            cls._custom_select_method(cls._LOCATOR_AREA_NAME, text=area_name)

    @classmethod
    def _set_commerce_plan(cls, commerce_plan):
        with testit.step(f'Set commerce plan {commerce_plan} in form b2c creation name'):
            Input(cls._LOCATOR_BUILDING_COMMERCE_PLAN).input(commerce_plan)


    @classmethod
    def _set_parameters_new_building(cls, smr: dict):
        cls._set_building_type(smr['building_type'])
        cls._set_location(smr['location_name'])
        cls._set_random_street_and_house()
        cls._set_object_type(smr['obj_type'])
        cls._set_client(smr['client'])
        cls._set_building_fields(smr['floors'], smr['entrances'], smr['flats'], smr['dh_counter'],
                                  smr['commerce_plan'])
        cls._set_building_ap_years(smr['ap_year'])


    @classmethod
    def _set_parameters_private_sector(cls, smr: dict):
        cls._set_building_type(smr['building_type'])
        cls._set_location(smr['location_name'])
        cls._set_area(smr['area'])
        cls._set_village(smr['village'])
        cls._set_area_name(smr['area_name'])
        if cls._is_error_add_address_on_creation_order:
            cls._delete_creating_orders()
            raise 'Заявка B2C удалена по данному адресу, необходимо повторно выполнить тест'
        cls._set_commerce_plan(smr['commerce_plan'])
        cls._set_building_ap_years(smr['ap_year'])


    @classmethod
    @testit.step('Create smr order')
    def create_smr_order_form(self, smr: dict):
        if smr['building_type'] == 'Комплексная новостройка':
            self._set_parameters_new_building(smr)
        if smr['building_type'] == 'Коттеджный посёлок/частный сектор':
            self._set_parameters_private_sector(smr)
        self._create_order()


    @classmethod
    @testit.step('Get created order')
    def get_creation_order(cls) -> int:
        smr_order_id = int(Locator(cls._LOCATOR_CREATION_ORDER).text)
        with testit.step(f'Get creation order {smr_order_id} in form b2c creation name'):
            return smr_order_id
