import random
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class B2CCreateConstructionProjectShow(BasePage):
    _LOCATOR_SELECT_RF = (By.CSS_SELECTOR, 'select#rfId')
    _LOCATOR_SELECT_IS_NEED_BROAD_BAND = (By.CSS_SELECTOR, '#needBroadband')
    _LOCATOR_SELECT_TYPE_BUILD_TYPE = (By.CSS_SELECTOR, '#buildTypeId')
    _LOCATOR_SELECT_AJAX_CUSTOMER = (By.CSS_SELECTOR, '#customerId')
    _LOCATOR_SELECT_TECHNOLOGY = (By.CSS_SELECTOR, '#technology')
    _LOCATOR_INPUT_PROJECT_NAME = (By.CSS_SELECTOR, '#projectName')
    _LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR = (By.CSS_SELECTOR, '.btn-group button')
    _LOCATOR_OPEN_DROPDOWN = (By.XPATH, '//div[@class = "suggest form-control input-sm"]')

    _LOCATOR_SELECT_AJAX_MODAL = (By.CSS_SELECTOR, '.modal-content')
    _LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY = (By.CSS_SELECTOR, '.modal-content [id^=city]')
    _LOCATOR_SELECT_AJAX_MODAL_ADDRESS_STREET = (
        By.CSS_SELECTOR, '.modal-content .js--b2c-construction-projects-load-houses-on-street')
    _LOCATOR_SELECT_MODAL_ADDRESS_LIST_UNCHECKED = (
        By.CSS_SELECTOR, '.modal-content .construction-projects-address-div div:first-child select')
    _LOCATOR_SELECT_MODAL_ADDRESS_LIST_CHECKED = (
        By.CSS_SELECTOR, '.modal-content .construction-projects-address-div div:last-child select')
    _LOCATOR_BUTTON_MODAL_ADDRESS_ADD_ADDRESS = (
        By.CSS_SELECTOR, '.modal-content .construction-projects-address-div .js--b2c-multi-selected-values-right')
    _LOCATOR_BUTTON_MODAL_ADDRESS_DELETE_ADDRESS = (
        By.CSS_SELECTOR, '.modal-content .construction-projects-address-div .js--b2c-multi-selected-values-left')
    _LOCATOR_BUTTON_MODAL_ADDRESS_CONFIRM_ADDRESS = (
        By.CSS_SELECTOR, '.modal-content .js--b2c-construction-projects-add-selected-addresses')
    _LOCATOR_BUTTON_MODAL_ADDRESS_CLOSE_MODAL = (By.CSS_SELECTOR, '.modal-content [data-dismiss="modal"]:last-child')

    _LOCATOR_TABLE_SERVICES = (By.CSS_SELECTOR, '.b2c-create-construction-project-objects')
    _LOCATOR_TABLE_SERVICES_OPEN_DH = (By.CSS_SELECTOR, '.b2c-objects :nth-child(7)')
    _LOCATOR_TABLE_SERVICES_ENTER_DH = (By.CSS_SELECTOR, '.b2c-objects :nth-child(7) input')

    _LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES = (By.CSS_SELECTOR, '.b2c-objects :nth-child(8)')

    _LOCATOR_CHECKBOX_MODAL_SERVICES_LIST = (By.CSS_SELECTOR, '.modal-body .b2c-service-group:nth-child(2) input')
    _LOCATOR_CHECKBOX_MODAL_SERVICE = (By.XPATH, '//div[@class="b2c-service-name"')
    _LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT = (By.CSS_SELECTOR, '.js--b2c-construction-btn-save-key-services')
    _LOCATOR_BUTTON_MODAL_SERVICES_CLOSE_MODAL = (
        By.CSS_SELECTOR, '.b2c-construction-projects-modal-services .modal-dialog .modal-footer button')

    _LOCATOR_BUTTON_DELETE_SERVICES = (By.CSS_SELECTOR, '.js--b2c-construction-projects-delete-objects')
    _LOCATOR_BUTTON_CREATE_PROJECT = (By.CSS_SELECTOR, '.js--b2c-construction-projects-create-project')

    def selected_rf(self, rf_name: str):
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_RF, value=rf_name)

    def selected_type_construct(self, value: str):
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_TYPE_BUILD_TYPE, value=value)

    def selected_is_need_broad(self, is_need_broad: str = 'Нет'):
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_IS_NEED_BROAD_BAND,
                                       value=is_need_broad)

    def selected_customer_by_inn(self, value):
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_AJAX_CUSTOMER,
                                       value=value)

    def enter_project_name(self, value):
        self.find_element(locator=self._LOCATOR_INPUT_PROJECT_NAME).send_keys(
            f'{value} (уникальный: {time.time()})')

    def add_address(self, city_name, street_name, house):
        self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR).click()
        self.find_element(locator=self._LOCATOR_OPEN_DROPDOWN).click()
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY,
                                       value=city_name)
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_STREET,
                                       value=street_name)
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_MODAL_ADDRESS_LIST_UNCHECKED, value=house)
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADDRESS_ADD_ADDRESS).click()
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADDRESS_CONFIRM_ADDRESS).click()

    def enter_dh_for_address(self, dh_count):
        self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_DH).click()
        self.find_element(locator=self._LOCATOR_TABLE_SERVICES_ENTER_DH).send_keys(f'{dh_count}\n')

    def set_random_service_key(self):
        self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).is_displayed()
        time.sleep(3)
        self.find_elements(locator=self._LOCATOR_CHECKBOX_MODAL_SERVICES_LIST)[random.randint(0, 5)].click()
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    def set_service_key(self, service_name: str):
        selector = f'{self._LOCATOR_CHECKBOX_MODAL_SERVICE[1]} and contains(., "{service_name}")]//input'

        self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
        time.sleep(3)
        self.find_element(locator=(By.XPATH, selector)).click()
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    def enter_create_project(self):
        self.find_element(locator=self._LOCATOR_BUTTON_CREATE_PROJECT).click()
