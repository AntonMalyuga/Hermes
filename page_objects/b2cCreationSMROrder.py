import random
from page_objects.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import keyboard


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
                       '//label[@for= "ADDRESS[ATDSTREET]"]/ancestor::div[2]//div[@class = "suggest form-control select-service-address input-sm"]')
    _LOCATOR_HOUSE = (By.XPATH,
                       '//label[@for= "ADDRESS[ATDHOUSE]"]/ancestor::div[2]//div[@class = "suggest form-control select-service-address input-sm"]')

    _LOCATOR_CLIENT = (By.XPATH, '//div[@style = "display: flex"]//div[@class= "suggest form-control input-sm js--matomo-log-focus-event"]')
    _LOCATOR_OBJECT_TYPE = (By.XPATH,
                       '//div[@class = "form-group has-warning"]//div[@class = "suggest form-control select-service-address input-sm"]')
    _LOCATOR_WIFI_CHECKBOX = (By.XPATH, '//div[@class= "b2c-service-group"]//input[@name= "services[wifi]"]')
    _LOCATOR_CREATE_BUTTON = (By.XPATH, '//button[@class= "btn btn-primary"]')

    def fill_ugly_forms(self, locator, text):
        self.find_element(locator=locator).click()
        keyboard.write(text)
        time.sleep(1)
        keyboard.press_and_release('enter')
        keyboard.press_and_release('tab')

    def fill_bilding_type(self, building_type):
        Select(self.find_element(locator=self._LOCATOR_BUILDING_TYPE)).select_by_visible_text(building_type)

    def fill_location(self, location_name):
        time.sleep(1)
        self.fill_ugly_forms(locator=self._LOCATOR_LOCATION, text=location_name)

    def fill_street(self, street_name):
        self.fill_ugly_forms(locator=self._LOCATOR_STREET, text=street_name)

    def fill_house(self, house_name):
        time.sleep(1)
        self.fill_ugly_forms(locator=self._LOCATOR_HOUSE, text=house_name)

    def fill_client(self, client):
        self.fill_ugly_forms(locator=self._LOCATOR_CLIENT, text=client)

    def fill_object_type(self, obj_type):
        self.fill_ugly_forms(locator=self._LOCATOR_OBJECT_TYPE, text=obj_type)

    def fill_building_fields(self, floors, entrances, flats, dh_counter, commerce_plan):
        self.find_element(locator=self._LOCATOR_BUILDING_FLOORS).send_keys(floors)
        self.find_element(locator=self._LOCATOR_BUILDING_ENTRANCES).send_keys(entrances)
        self.find_element(locator=self._LOCATOR_BUILDING_FLAT_AT_FLOOR).send_keys(flats)
        self.find_element(locator=self._LOCATOR_BUILDING_DH_COUNTER).send_keys(dh_counter)
        self.find_element(locator=self._LOCATOR_BUILDING_COMMERCE_PLAN).send_keys(commerce_plan)

    def fill_building_ap_years(self, ap_year):
        self.fill_ugly_forms(locator=self._LOCATOR_BUILDING_AP_YEAR, text=ap_year)

    def fill_wifi_checkbox(self):
        self.find_element(locator=self._LOCATOR_WIFI_CHECKBOX).click()

    def create_order(self):
        self.find_element(locator=self._LOCATOR_CREATE_BUTTON).click()

    def create_smr_order_form(self, smr: dict):
        self.fill_bilding_type(smr['building_type'])
        self.fill_location(smr['location_name'])
        self.fill_street(smr['street_name'])
        self.fill_house(smr['house_name'])
        self.fill_client(smr['client'])
        self.fill_object_type(smr['obj_type'])
        self.fill_building_fields(smr['floors'], smr['entrances'], smr['flats'], smr['dh_counter'], smr['commerce_plan'])
        self.fill_building_ap_years(smr['ap_year'])
        self.fill_wifi_checkbox()
        # self.create_order()
