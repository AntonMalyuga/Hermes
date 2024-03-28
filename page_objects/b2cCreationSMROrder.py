from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import time


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

    def is_mistake(self):
        try:
            return len(self.find_elements(locator=self._LOCATOR_MISTAKE, second=2)) >= 1
        except:
            return False

    def _custom_select_method(self, locator, text):
        element = self.find_element(locator)
        locator_input = self.find_element((By.XPATH, f'{locator[1]}//input[@type="text"]'))
        element.click()
        locator_input.send_keys(text)
        time.sleep(1)
        locator_input.send_keys('\n')

    def set_building_type(self, building_type: str):
        Select(self.find_element(locator=self._LOCATOR_BUILDING_TYPE)).select_by_visible_text(building_type)

    def set_location(self, location_name: str):
        time.sleep(2)
        self._custom_select_method(locator=self._LOCATOR_LOCATION, text=location_name)

    def get_streets_name(self):
        time.sleep(2)
        elements = self.find_elements(locator=self._LOCATOR_ELEMENTS_STREETS)
        street_names = [element.get_property('innerText') for element in elements]
        return street_names

    def get_house_names(self):
        time.sleep(2)
        elements = self.find_elements(locator=self._LOCATOR_ELEMENTS_HOUSES)
        house_names = [element.get_property('innerText') for element in elements]
        return house_names

    def set_random_street_and_house(self):
        streets_name = self.get_streets_name()
        for street_name in streets_name:
            self._custom_select_method(locator=self._LOCATOR_STREET, text=street_name)
            time.sleep(2)
            first_police_house = self.get_police_house()
            if first_police_house:
                self.set_house(first_police_house)
                time.sleep(2)
                if self.is_mistake():
                    continue
                else:
                    break

    def get_police_house(self):
        houses = self.find_elements(locator=self._LOCATOR_ELEMENTS_HOUSES)
        for house in houses:
            house_name = house.get_property('innerText')
            if str(house_name).find('Милицейские') == -1:
                continue
            else:
                return house_name
        return False

    def set_house(self, house_name: str):
        time.sleep(1)
        self._custom_select_method(locator=self._LOCATOR_HOUSE, text=house_name)

    def set_client(self, client: str):
        keyboard = Controller()
        self._custom_select_method(locator=self._LOCATOR_CLIENT, text=client)
        time.sleep(3)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    def set_object_type(self, obj_type: str):
        self._custom_select_method(locator=self._LOCATOR_OBJECT_TYPE, text=obj_type)

    def set_building_fields(self, floors: int, entrances: int, flats: int, dh_counter: int, commerce_plan: int):
        def clear_and_set(locator, value):
            self.find_element(locator=locator).clear()
            self.find_element(locator=locator).send_keys(value)

        clear_and_set(locator=self._LOCATOR_BUILDING_ENTRANCES, value=entrances)
        clear_and_set(locator=self._LOCATOR_BUILDING_FLOORS, value=floors)
        clear_and_set(locator=self._LOCATOR_BUILDING_FLAT_AT_FLOOR, value=flats)
        clear_and_set(locator=self._LOCATOR_BUILDING_DH_COUNTER, value=dh_counter)
        clear_and_set(locator=self._LOCATOR_BUILDING_COMMERCE_PLAN, value=commerce_plan)

    def set_building_ap_years(self, ap_year: int):
        self._custom_select_method(locator=self._LOCATOR_BUILDING_AP_YEAR, text=ap_year)

    def set_wifi_checkbox(self):
        self.find_element(locator=self._LOCATOR_WIFI_CHECKBOX).click()

    def create_order(self):
        self.find_element(locator=self._LOCATOR_CREATE_BUTTON).click()

    def set_area(self, area: str):
        time.sleep(1)
        self._custom_select_method(locator=self._LOCATOR_AREA, text=area)

    def set_village(self, village: str):
        time.sleep(1)
        self._custom_select_method(locator=self._LOCATOR_VILLAGE, text=village)

    def set_area_name(self, area_name):
        time.sleep(1)
        self._custom_select_method(locator=self._LOCATOR_AREA_NAME, text=area_name)

    def set_commerce_plan(self, commerce_plan):
        self.find_element(locator=self._LOCATOR_BUILDING_COMMERCE_PLAN).send_keys(commerce_plan)

    def create_smr_order_form(self, smr: dict):
        if smr['building_type'] == 'Комплексная новостройка':
            time.sleep(2)
            self.set_building_type(smr['building_type'])
            self.set_location(smr['location_name'])
            self.set_random_street_and_house()
            self.set_object_type(smr['obj_type'])
            self.set_client(smr['client'])
            self.set_building_fields(smr['floors'], smr['entrances'], smr['flats'], smr['dh_counter'],
                                     smr['commerce_plan'])
            self.set_building_ap_years(smr['ap_year'])
            self.create_order()
        if smr['building_type'] == 'Коттеджный посёлок/частный сектор':
            self.set_building_type(smr['building_type'])
            self.set_location(smr['location_name'])
            self.set_area(smr['area'])
            self.set_village(smr['village'])
            self.set_area_name(smr['area_name'])
            self.set_commerce_plan(smr['commerce_plan'])
            self.set_building_ap_years(smr['ap_year'])
            self.create_order()
        time.sleep(3)

    def get_creation_order(self) -> int:
        self.check_loader()
        return int(self.find_element(self._LOCATOR_CREATION_ORDER).text)
