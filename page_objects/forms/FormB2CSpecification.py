import time
import testit
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


class B2cFormSpecification:

    name = 'Редактировать спецификацию оборудования B2C'

    _LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION = 'button[id="addEquipment"]')
    _LOCATOR_CHECK_OPEN_MODAL = '.modal.fade.in')
    _LOCATOR_SHOW_MODAL_SPECIFICATION_LIST = (By.XPATH, '//button[@data-url="/b2c/specification/equipment_list"]')
    _LOCATOR_TABLE_INSERT_SPECIFICATION = (
        By.XPATH, '//div[@id="specification-equipment-list"]/table')
    _LOCATOR_BUTTON_SAVE_WORKS = 'button.btn.btn-primary.js--validation-hidden-forms')
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = (By.XPATH, '//label[@class="radio-inline"')
    _LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION = (
        By.XPATH, '//button[@class[contains(.,"b2c-specification-add-equipments")]]')
    _LOCATOR_BUTTON_MODAL_CLOSE = (
        By.XPATH, '//div[@class[contains(.,"specification-modal-controls")]]/button[@data-dismiss="modal"]')
    _LOCATOR_BUTTON_CREATE_SPECIFICATION = (
        By.XPATH, '//form[@id[contains(., "specification")]]/button[contains(., "Создать спецификацию")]')

    def __set_construct_method(self, type_construct):
        with testit.step(f'Выбрать метод строительства "{type_construct}" с помощью B2C спецификации', 'Тип строительства выбран'):
            selector = f'{self._LOCATOR_LABEL_CONSTRUCTION_METHOD[1]} and contains(.,"{type_construct}")]/input'
            element = self.find_element(locator=(By.XPATH, selector))

            try:
                element.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", element)

    def __open_modal(self):
        with testit.step('Открыть модальное окно в спецификации'):
            element = self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION)
            try:
                element.click()
            except ElementClickInterceptedException:
                self._driver.execute_script("arguments[0].click()", element)

            def check_open_modal():
                return self.find_element(self._LOCATOR_CHECK_OPEN_MODAL)

            check_open_modal()

    def __close_modal(self):
        with testit.step('Закрыть модальное окно', 'Окно закрыто'):
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_CLOSE).click()

    def __confirm_selected_specification(self):
        with testit.step('Подтвердить выбранную спецификацию'):
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION).click()

    def __show_specification_list_by_modal(self):
        with testit.step('Показать список спецификаций'):
            self.find_element(self._LOCATOR_SHOW_MODAL_SPECIFICATION_LIST).click()

    def __add_specification_by_modal(self, specifications: dict):
        for specification, specification_param in specifications.items():
            with testit.step(f'Выбрать спецификацию "{specification}" в модальном окне формы спецификации'):
                element = self.find_element((By.XPATH,
                                             f'{self._LOCATOR_TABLE_INSERT_SPECIFICATION[1]}//td[@data-name="name" and contains(.,"{specification}")]/ancestor::tr[1]//input'))
                try:
                    element.click()
                except ElementClickInterceptedException:
                    self._driver.execute_script("arguments[0].click()", element)

        self.__confirm_selected_specification()
        self.__close_modal()

    def __set_method_by_specification(self, specification: dict):
        for specification, specification_params in specification.items():
            with testit.step(f'Установить метод строительства "{specification}" в спецификации'):
                time.sleep(1)
                specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification}")]/following::td[11]/select[@name[contains(., "type_installation")]]'
                self.selected_element_by_value(locator=(By.XPATH, specification_locator),
                                               value=specification_params["method"])

    def __set_natural_indicators(self, specification: dict):
        for specification, specification_params in specification.items():
            with testit.step(f'Установить натуральные показатели "{specification}" в спецификации'):
                time.sleep(1)
                specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification}")]/following::td[1]/select[@id[contains(., "naturalIndicator")]]'
                self.selected_element_by_value(locator=(By.XPATH, specification_locator),
                                               value=specification_params["natural_indicator"])

    def __create_specification(self):
        with testit.step('Нажать кнопку создания спецификации'):
            self.find_element(locator=self._LOCATOR_BUTTON_CREATE_SPECIFICATION).click()

    def add_specification(self, specifications: dict):
        with testit.step('Добавить спецификацию', 'Спецификация сохранена'):
            self.__set_construct_method(specifications['constuct_method'])
            self.__open_modal()
            self.__show_specification_list_by_modal()

            if 'specifications_keys' in specifications:
                self.__add_specification_by_modal(specifications['specifications_keys'])
                self.__set_natural_indicators(specifications['specifications_keys'])
            if 'specifications_core' in specifications:
                self.__add_specification_by_modal(specifications['specifications_core'])
                self.__set_method_by_specification(specifications['specifications_core'])
            self.__create_specification()
