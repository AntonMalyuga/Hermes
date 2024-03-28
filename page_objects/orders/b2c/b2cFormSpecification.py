import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class B2cFormSpecification(BasePage):
    _LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION = (By.CSS_SELECTOR, 'button[id="addEquipment"]')
    _LOCATOR_CHECK_OPEN_MODAL = (By.CSS_SELECTOR, '.modal.fade.in')
    _LOCATOR_CHECK_SHOW_MODAL_SPECIFICATION_LIST = (By.XPATH, '//button[@data-url="/b2c/specification/equipment_list"]')
    _LOCATOR_TABLE_INSERT_SPECIFICATION = (
        By.XPATH, '//div[@id="specification-equipment-list"]/table')
    _LOCATOR_BUTTON_SAVE_WORKS = (By.CSS_SELECTOR, 'button.btn.btn-primary.js--validation-hidden-forms')
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = (By.XPATH, '//label[@class="radio-inline"')
    _LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION = (
        By.XPATH, '//button[@class[contains(.,"b2c-specification-add-equipments")]]')
    _LOCATOR_BUTTON_MODAL_CLOSE = (
        By.XPATH, '//div[@class[contains(.,"specification-modal-controls")]]/button[@data-dismiss="modal"]')
    _LOCATOR_BUTTON_CREATE_SPECIFICATION = (
        By.XPATH, '//form[@id[contains(., "specification")]]/button[contains(., "Создать спецификацию")]')

    def set_construct_method(self, type_construct):

        selector = f'{self._LOCATOR_LABEL_CONSTRUCTION_METHOD[1]} and contains(.,"{type_construct}")]/input'
        element = self.find_element(locator=(By.XPATH, selector))

        try:
            element.click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click()", element)

    def check_open_modal(self):
        return self.find_element(self._LOCATOR_CHECK_OPEN_MODAL)

    def open_modal(self):
        element = self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION)
        try:
            element.click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click()", element)

    def close_modal(self):
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_CLOSE).click()

    def confirm_selected_specification(self):
        self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION).click()

    def add_specification(self, specifications: dict):
        self.open_modal()
        self.check_open_modal()
        self.find_element(self._LOCATOR_CHECK_SHOW_MODAL_SPECIFICATION_LIST).click()

        if 'specifications_keys' in specifications:
            self.add_specification_by_modal(specifications['specifications_keys'])
            self.set_natural_indicators(specifications['specifications_keys'])
        if 'specifications_core' in specifications:
            self.add_specification_by_modal(specifications['specifications_core'])
            self.set_method_by_specification(specifications['specifications_core'])
        self.create_specification()

    def add_specification_by_modal(self, specifications: dict):
        for specification, specification_param in specifications.items():
            element = self.find_element((By.XPATH,
                                         f'{self._LOCATOR_TABLE_INSERT_SPECIFICATION[1]}//td[@data-name="name" and contains(.,"{specification}")]/ancestor::tr[1]//input'))
            try:
                element.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", element)

        self.confirm_selected_specification()
        self.close_modal()

    def set_method_by_specification(self, specification: dict):
        for specification, specification_params in specification.items():
            time.sleep(1)
            specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification}")]/following::td[11]/select[@name[contains(., "type_installation")]]'
            self.selected_element_by_value(locator=(By.XPATH, specification_locator),
                                           value=specification_params["method"])

    def set_natural_indicators(self, specification: dict):
        for specification, specification_params in specification.items():
            time.sleep(1)
            specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification}")]/following::td[1]/select[@id[contains(., "naturalIndicator")]]'
            self.selected_element_by_value(locator=(By.XPATH, specification_locator),
                                           value=specification_params["natural_indicator"])

    def create_specification(self):
        self.find_element(locator=self._LOCATOR_BUTTON_CREATE_SPECIFICATION).click()
