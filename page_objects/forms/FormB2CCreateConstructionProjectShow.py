import random
import testit
from selenium.webdriver.common.by import By
import time


class FormB2CCreateConstructionProjectShow:
    name = 'Создать строительный проект B2C'
    path = 'b2c/create_construction_project_show'

    _LOCATOR_SELECT_RF = 'select#rfId')
    _LOCATOR_SELECT_IS_NEED_BROAD_BAND = '#needBroadband')
    _LOCATOR_SELECT_TYPE_BUILD_TYPE = '#buildTypeId')
    _LOCATOR_SELECT_AJAX_CUSTOMER = '#customerId')
    _LOCATOR_SELECT_TECHNOLOGY = '#technology')
    _LOCATOR_INPUT_PROJECT_NAME = '#projectName')
    _LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR = '.btn-group button')
    _LOCATOR_OPEN_DROPDOWN = (By.XPATH, '//div[@class = "suggest form-control input-sm"]')

    _LOCATOR_SELECT_AJAX_MODAL = '.modal-content')
    _LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY = (By.XPATH, '//div[@class="modal-content"]//input[contains(@id, "city")]')
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
    _LOCATOR_BUTTON_MODAL_ADDRESS_CLOSE_MODAL = '.modal-content [data-dismiss="modal"]:last-child')

    _LOCATOR_TABLE_SERVICES = '.b2c-create-construction-project-objects')
    _LOCATOR_TABLE_SERVICES_OPEN_DH = '.b2c-objects :nth-child(7)')
    _LOCATOR_TABLE_SERVICES_ENTER_DH = '.b2c-objects :nth-child(7) input')

    _LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES = '.b2c-objects :nth-child(8)')

    _LOCATOR_CHECKBOX_MODAL_SERVICES_LIST = '.modal-body .b2c-service-group:nth-child(2) input')
    _LOCATOR_CHECKBOX_MODAL_SERVICE = (By.XPATH, '//div[@class="b2c-service-name"')
    _LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT = '.js--b2c-construction-btn-save-key-services')
    _LOCATOR_BUTTON_MODAL_SERVICES_CLOSE_MODAL = (
        By.CSS_SELECTOR, '.b2c-construction-projects-modal-services .modal-dialog .modal-footer button')

    _LOCATOR_BUTTON_DELETE_SERVICES = '.js--b2c-construction-projects-delete-objects')
    _LOCATOR_BUTTON_CREATE_PROJECT = '.js--b2c-construction-projects-create-project')

    def _selected_rf(self, rf_name: str):
        with testit.step(f'Установить региональный филиал "{rf_name}"'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_RF, value=rf_name)

    def _selected_type_construct(self, type_construct: str):
        with testit.step(f'Установить тип строительства "{type_construct}"'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_TYPE_BUILD_TYPE, value=type_construct)

    def _selected_is_need_broad(self, is_need_broad: str = 'Нет'):
        with testit.step(f'Установить статус "требуется строительство ШПД" "{is_need_broad}"'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_IS_NEED_BROAD_BAND,
                                           value=is_need_broad)

    def _selected_customer_by_inn(self, inn: str):
        with testit.step(f'Выбрать клиента по ИНН: "{inn}"'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_AJAX_CUSTOMER,
                                           value=inn)

    def _enter_project_name(self, project_name: str):
        unique_project_name = f'{project_name} (уникальный: {time.time()})'
        with testit.step(f'Установить имя проекта: "{project_name}"'):
            self.find_element(locator=self._LOCATOR_INPUT_PROJECT_NAME).send_keys(unique_project_name)

    def _set_modal_address_city(self, address_city):

        locator = self._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY

        with testit.step(f'Установить адрес в модальном окне "{address_city}"'):
            self.find_element(locator=self._LOCATOR_OPEN_DROPDOWN).click()
            self.find_element(f'{locator[1]}/following::div[1]')).click()
            time.sleep(2)
            self.find_element(f'{locator[1]}/following::div[1]//input[@type="text"]')).send_keys(
                address_city)
            time.sleep(2)
            self.find_element((By.CSS_SELECTOR,
                               f'{locator[1]}/following::div[1]//span/span[ontains(text(), "Город {address_city}")]')).click()

    def _set_modal_address_street(self, street_name: str):
        with testit.step(f'Установить улицу в модальном окне: {street_name}'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_STREET,
                                       value=street_name)

    def _set_modal_address_house(self, house_name: str):
        with testit.step(f'Установить дом в модальном окне: {house_name}'):
            self.selected_element_by_value(locator=self._LOCATOR_SELECT_MODAL_ADDRESS_LIST_CHECKED, value=house_name)
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADDRESS_ADD_ADDRESS).click()
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_ADDRESS_CONFIRM_ADDRESS).click()

    def _open_modal_address(self):
        with testit.step(f'Открыть модальное окно'):
            self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR).click()

    def _add_address(self, city_name, street_name, house):
        with testit.step(f'Установить адрес "{city_name}", "{street_name}" and "{house}"'):
            self._open_modal_address()
            self._set_modal_address_city(address_city=city_name)
            self._set_modal_address_street(street_name=street_name)
            self._set_modal_address_house(house_name=house)

    def _enter_dh_for_address(self, dh_count):
        with testit.step(f'Установить количество ДХ "{dh_count}"'):
            self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_DH).click()
            self.find_element(locator=self._LOCATOR_TABLE_SERVICES_ENTER_DH).send_keys(f'{dh_count}\n')

    def _set_random_service_key(self):
        with testit.step('Установить рандомный сервисный ключ', 'Сервисный ключ установлен'):
            self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).is_displayed()
            time.sleep(3)
            self.find_elements(locator=self._LOCATOR_CHECKBOX_MODAL_SERVICES_LIST)[random.randint(0, 5)].click()
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    def _set_service_key(self, service_name: str):
        with testit.step(f'Установить услугу "{service_name}"'):
            selector = f'{self._LOCATOR_CHECKBOX_MODAL_SERVICE[1]} and contains(., "{service_name}")]//input'

            self.find_element(locator=self._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
            time.sleep(3)
            self.find_element(locator=(By.XPATH, selector)).click()
            self.find_element(locator=self._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    def _enter_create_project(self):
        with testit.step('Кликнуть кнопку проект', 'Проект создан'):
            self.find_element(locator=self._LOCATOR_BUTTON_CREATE_PROJECT).click()

    def create_project(self, project: dict, is_prepared: bool = False):
        with testit.step('Создать проект', 'Проект создан'):
            if is_prepared:
                self._enter_project_name(project['project_name'])
                self._enter_create_project()
            else:
                self._selected_rf(project['rf'])
                self._selected_is_need_broad(project['is_need_broad'])
                self._selected_type_construct(project['is_type_construct'])
                self._selected_customer_by_inn(project['customer_inn'])
                self._enter_project_name(project['project_name'])
                self._add_address(project['address']['city'], project['address']['street'],
                                  project['address']['house_name'])
                self._enter_dh_for_address(project['dh'])
                self._set_service_key(project['service_key'])
                self._enter_create_project()
