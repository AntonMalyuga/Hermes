from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pynput.keyboard import Key, Controller
import time
import testit


class B2CCreateSMROrder(BasePage):
    path = 'client/createb2c'

    _LOCATOR_BUILDING_TYPE = (
        By.XPATH, '//select[@class= "form-control input-sm input-reload-onchange suggest__hidden-accessible"]')
    _LOCATOR_BUILDING_FLOORS = (By.XPATH, '//input[@id[contains(., "ADDRESSPARAMS[MAX_ETAZH]")]]')
    _LOCATOR_BUILDING_ENTRANCES = (By.XPATH, '//input[@id[contains(., "ADDRESSPARAMS[CNT_PODJEZD]")]]')
    _LOCATOR_BUILDING_FLAT_AT_FLOOR = (By.XPATH, '//input[@id[contains(., "ADDRESSPARAMS[FLAT_AT_FLOOR]")]]')
    _LOCATOR_BUILDING_DH_COUNTER = (By.XPATH, '//input[@id[contains(., "ADDRESSPARAMS[COUNT_FLATS]")]]')
    _LOCATOR_BUILDING_COMMERCE_PLAN = (By.XPATH, '//input[@id[contains(., "ADDRESSPARAMS[PP_DRS]")]]')
    _LOCATOR_BUILDING_AP_YEAR = (By.XPATH,
                                 '//div[@class = "form-group  has-warning"]//div[@class = "suggest form-control input-sm js--matomo-log-focus-event"]')

    _LOCATOR_LOCATION = (By.XPATH, '//div[@class = "suggest form-control select-service-address input-sm"]')
    _LOCATOR_STREET = (By.XPATH,
                       '//label[@for= "ADDRESS[ATDSTREET]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]')

    _LOCATOR_HOUSE = (By.XPATH,
                      '//label[@for= "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//div[@class = "suggest form-control select-service-address input-sm"]')

    _LOCATOR_CLIENT = (By.XPATH,
                       '//div[@style = "display: flex"]//div[@class= "suggest form-control input-sm js--matomo-log-focus-event"]')
    _LOCATOR_OBJECT_TYPE = (By.XPATH,
                            '//div[@class = "form-group has-warning"]//div[@class = "suggest form-control select-service-address input-sm"]')
    _LOCATOR_OBJECT_TYPE_DISABLED = (By.XPATH, '//select[@name = "ADDRESS[CRM_OBJECT_TYPE]"]')
    _LOCATOR_WIFI_CHECKBOX = (By.XPATH, '//div[@class= "b2c-service-group"]//input[@name= "services[wifi]"]')
    _LOCATOR_CREATE_BUTTON = (By.XPATH, '//button[@class= "btn btn-primary"]')
    _LOCATOR_ELEMENTS_HOUSES = (By.XPATH, '//label[@for = "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//span[@class = "name"]')
    _LOCATOR_ELEMENTS_STREETS = (
        By.XPATH, '//label[@for = "ADDRESS[ATDSTREET]"]/ancestor::div[2]//span[@class = "name"]')
    _LOCATOR_CREATION_ORDER = (By.CSS_SELECTOR, '#CreateOrderb2C a')
    _LOCATOR_AREA = (By.XPATH,
                     '//label[@for= "ADDRESS[ATDOBJECT][1]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]')
    _LOCATOR_VILLAGE = (By.XPATH,
                        '//label[@for= "ADDRESS[ATDOBJECT][2]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]')
    _LOCATOR_AREA_NAME = (By.XPATH,
                          '//label[@for= "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//div[@class[contains(., "suggest form-control select-service-address input-sm")]]')
    _LOCATOR_MISTAKE = (By.XPATH, '//h5[@class = "text-danger"]')

    @testit.step('Check error add creation order by address in form b2c creation smr')
    def _is_error_add_address_on_creation_order(self):
        try:
            return len(self.find_elements(locator=self._LOCATOR_MISTAKE, second=2)) >= 1
        except:
            return False

    def _custom_select_method(self, locator, text):
        with testit.step(f'Custom select value {text} by {locator} in form b2c creation smr'):
            element = self.find_element(locator)
            locator_input = self.find_element((By.XPATH, f'{locator[1]}//input[@type="text"]'))
            element.click()
            locator_input.send_keys(text)
            time.sleep(1)
            locator_input.send_keys('\n')

    def _set_building_type(self, building_type: str):
        with testit.step(f'Set building type {building_type} in form b2c creation smr'):
            Select(self.find_element(locator=self._LOCATOR_BUILDING_TYPE)).select_by_visible_text(building_type)

    def _set_location(self, location_name: str):
        time.sleep(2)
        with testit.step(f'Set location {location_name} in form b2c creation smr'):
            self._custom_select_method(locator=self._LOCATOR_LOCATION, text=location_name)

    @testit.step('Get streets names in form b2c creation smr')
    def _get_streets_name(self):
        time.sleep(2)
        elements = self.find_elements(locator=self._LOCATOR_ELEMENTS_STREETS)
        street_names = [element.get_property('innerText') for element in elements]
        return street_names

    @testit.step('Get houses names in form b2c creation smr')
    def _get_house_names(self):
        time.sleep(2)
        elements = self.find_elements(locator=self._LOCATOR_ELEMENTS_HOUSES)
        house_names = [element.get_property('innerText') for element in elements]
        return house_names

    def _set_random_street_and_house(self):
        streets_name = self._get_streets_name()
        for street_name in streets_name:
            self._custom_select_method(locator=self._LOCATOR_STREET, text=street_name)
            time.sleep(2)
            first_police_house = self._get_police_house()
            if first_police_house:
                self._set_house(first_police_house)
                time.sleep(2)
                if self._is_error_add_address_on_creation_order():
                    continue
                else:
                    with testit.step(f'Set ramdom street {first_police_house} and house in form b2c creation smr'):
                        break

    @testit.step('Get first police house in form b2c creation smr')
    def _get_police_house(self):
        houses = self.find_elements(locator=self._LOCATOR_ELEMENTS_HOUSES)
        for house in houses:
            house_name = house.get_property('innerText')
            if str(house_name).find('Милицейские') == -1:
                continue
            else:
                return house_name
        return False

    def _set_house(self, house_name: str):
        time.sleep(1)
        self._custom_select_method(locator=self._LOCATOR_HOUSE, text=house_name)

    def _set_client(self, client_name: str):
        with testit.step(f'Set client {client_name} in form b2c creation smr'):
            keyboard = Controller()
            self._custom_select_method(locator=self._LOCATOR_CLIENT, text=client_name)
            time.sleep(3)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

    def _set_object_type(self, obj_type: str):
        with testit.step('Set object type {obj_type} in form b2c creation smr'):
            self._custom_select_method(locator=self._LOCATOR_OBJECT_TYPE, text=obj_type)

    def _set_building_fields(self, floors: int, entrances: int, flats: int, dh_counter: int, commerce_plan: int):
        def clear_and_set(locator, value):
            self.find_element(locator=locator).clear()
            self.find_element(locator=locator).send_keys(value)

        with testit.step(
                f'Set building field {floors}, {entrances}, {flats}, {dh_counter} and {commerce_plan} in form b2c creation smr'):
            clear_and_set(locator=self._LOCATOR_BUILDING_ENTRANCES, value=entrances)
            clear_and_set(locator=self._LOCATOR_BUILDING_FLOORS, value=floors)
            clear_and_set(locator=self._LOCATOR_BUILDING_FLAT_AT_FLOOR, value=flats)
            clear_and_set(locator=self._LOCATOR_BUILDING_DH_COUNTER, value=dh_counter)
            clear_and_set(locator=self._LOCATOR_BUILDING_COMMERCE_PLAN, value=commerce_plan)

    def _set_building_ap_years(self, ap_year: int):
        with testit.step('Set building ap year {ap_year} in form b2c creation smr'):
            self._custom_select_method(locator=self._LOCATOR_BUILDING_AP_YEAR, text=ap_year)

    def _set_wifi_checkbox(self):
        with testit.step('Set checkbox wifi in form b2c creation name'):
            self.find_element(locator=self._LOCATOR_WIFI_CHECKBOX).click()

    def _create_order(self):
        with testit.step('Click create order in form b2c creation name'):
            self.find_element(locator=self._LOCATOR_CREATE_BUTTON).click()

    def _set_area(self, area: str):
        time.sleep(1)
        with testit.step('Set area {area} in form b2c creation name'):
            self._custom_select_method(locator=self._LOCATOR_AREA, text=area)

    def _set_village(self, village: str):
        time.sleep(1)
        with testit.step('Set village {village} in form b2c creation name'):
            self._custom_select_method(locator=self._LOCATOR_VILLAGE, text=village)

    def _set_area_name(self, area_name):
        time.sleep(1)
        with testit.step('Set area name {area_name} in form b2c creation name'):
            self._custom_select_method(locator=self._LOCATOR_AREA_NAME, text=area_name)

    def _set_commerce_plan(self, commerce_plan):
        with testit.step('Set commerce plan {commerce_plan} in form b2c creation name'):
            self.find_element(locator=self._LOCATOR_BUILDING_COMMERCE_PLAN).send_keys(commerce_plan)

    def _set_parameters_new_building(self, smr: dict):
        self._set_building_type(smr['building_type'])
        self._set_location(smr['location_name'])
        self._set_random_street_and_house()
        self._set_object_type(smr['obj_type'])
        self._set_client(smr['client'])
        self._set_building_fields(smr['floors'], smr['entrances'], smr['flats'], smr['dh_counter'],
                                  smr['commerce_plan'])
        self._set_building_ap_years(smr['ap_year'])

    def _set_parameters_private_sector(self, smr: dict):
        self._set_building_type(smr['building_type'])
        self._set_location(smr['location_name'])
        self._set_area(smr['area'])
        self._set_village(smr['village'])
        self._set_area_name(smr['area_name'])
        self._set_commerce_plan(smr['commerce_plan'])
        self._set_building_ap_years(smr['ap_year'])

    def create_smr_order_form(self, smr: dict):
        if smr['building_type'] == 'Комплексная новостройка':
            self._set_parameters_new_building(smr)
        if smr['building_type'] == 'Коттеджный посёлок/частный сектор':
            self._set_parameters_new_building(smr)
        self._create_order()
        with testit.step(f'Create smr order by template {smr}'):
            time.sleep(3)

    def get_creation_order(self) -> int:
        self.check_loader()
        smr_order_id = int(self.find_element(self._LOCATOR_CREATION_ORDER).text)
        with testit.step(f'Get creation order {smr_order_id} in form b2c creation name'):
            return smr_order_id
