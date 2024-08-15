from page import Page
import testit
import time
from dataclasses import dataclass
from locator import Locator, Select, Input


@dataclass
class Project:
    rf: str
    is_need_broad: str
    is_type_construct: str
    customer_inn: str
    project_name: str
    dh: int
    service_key: str


@dataclass
class Address:
    city: str = 'Ульяновск'
    street: str = 'Авиационная'
    house_name: str = 'д. 1'


class FormB2CCreateConstructionProjectShow(Page):
    name = 'Создать строительный проект B2C'
    path = 'b2c/create_construction_project_show'

    _LOCATOR_SELECT_RF = '//select[@id = "rfId"]'
    _LOCATOR_SELECT_IS_NEED_BROAD_BAND = '//select[@id = "needBroadband"]'
    _LOCATOR_SELECT_TYPE_BUILD_TYPE = '//input[@id = "buildTypeId"]'
    _LOCATOR_SELECT_AJAX_CUSTOMER = '//input[@id = "customerId"]'
    _LOCATOR_INPUT_PROJECT_NAME = '//input[@id = "projectName"]'
    _LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR = '.btn-group button'
    _LOCATOR_OPEN_DROPDOWN = '//button[contains(text(), "Добавить адрес в список")]'

    _MODAL = '//div[@class="modal-content"]'
    _LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY = f'{_MODAL}//input[contains(@id, "city")]'
    _LOCATOR_SELECT_AJAX_MODAL_ADDRESS_STREET = f'{_MODAL}//input[contains(@data-url, "streets_in_city")]'
    _LOCATOR_SELECT_MODAL_ADDRESS_LIST_UNCHECKED = f'{_MODAL}//div[contains(@class, "construction-projects-address-list")][1]//select'
    _LOCATOR_SELECT_MODAL_ADDRESS_LIST_CHECKED = f'{_MODAL}//div[contains(@class, "construction-projects-address-list")][2]//select'
    _LOCATOR_BUTTON_MODAL_ADDRESS_ADD_ADDRESS = f'{_MODAL}//button[./i[@class = "fas fa-arrow-right"]]'
    _LOCATOR_BUTTON_MODAL_ADDRESS_DELETE_ADDRESS = f'{_MODAL}//button[./i[@class = "fas fa-arrow-left"]]'
    _LOCATOR_BUTTON_MODAL_ADDRESS_CONFIRM_ADDRESS = f'{_MODAL}//button[contains(text(), "Добавить в список выбранные адреса")]'
    _LOCATOR_BUTTON_MODAL_ADDRESS_CLOSE_MODAL = f'{_MODAL}//button[text() = "Отмена"]'

    _TABLE_SERVICES = '//table[contains(@class, "b2c-create-construction-project-objects")]'
    _LOCATOR_TABLE_SERVICES_OPEN_DH = f'{_TABLE_SERVICES}//tr[@class="b2c-objects"]//td[7]'
    _LOCATOR_TABLE_SERVICES_ENTER_DH = f'{_LOCATOR_TABLE_SERVICES_OPEN_DH}/input'

    _LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES = f'{_TABLE_SERVICES}//tr[@class="b2c-objects"]//td[8]'

    _LOCATOR_CHECKBOX_MODAL_SERVICES_LIST = '//input[@name ="b2c-services"]'

    _LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT = '//button[contains(@class, "js--b2c-construction-btn-save-key-services")]'
    _LOCATOR_BUTTON_MODAL_SERVICES_CLOSE_MODAL = '//div[contains(@class, "b2c-construction-projects-modal-services")]//button[text() = "Отмена"]'

    _LOCATOR_BUTTON_DELETE_SERVICES = '//button[contains(text(), "Удалить выбранные объекты")]'
    _LOCATOR_BUTTON_CREATE_PROJECT = '//button[contains(text(), "Создать проект B2C")]'

    @classmethod
    def selected_rf(cls, rf_name: str):
        with testit.step(f'Установить региональный филиал "{rf_name}"'):
            Select(cls._LOCATOR_SELECT_RF).ajax_option(rf_name)

    @classmethod
    def selected_type_construct(cls, type_construct: str):
        with testit.step(f'Установить тип строительства "{type_construct}"'):
            Select(cls._LOCATOR_SELECT_TYPE_BUILD_TYPE).ajax_option(type_construct)

    @classmethod
    def selected_is_need_broad(cls, is_need_broad: str = 'Нет'):
        with testit.step(f'Установить статус "требуется строительство ШПД" "{is_need_broad}"'):
            Select(cls._LOCATOR_SELECT_IS_NEED_BROAD_BAND).option(is_need_broad)

    @classmethod
    def selected_customer_by_inn(cls, inn: str):
        with testit.step(f'Выбрать клиента по ИНН: "{inn}"'):
            Select(cls._LOCATOR_SELECT_AJAX_CUSTOMER).ajax_option(inn)

    @classmethod
    def enter_project_name(cls, project_name: str):
        unique_project_name = f'{project_name} (уникальный: {time.time()})'
        with testit.step(f'Установить имя проекта: "{project_name}"'):
            Input(cls._LOCATOR_INPUT_PROJECT_NAME).input(unique_project_name)

    @classmethod
    def set_modal_address_city(cls, address_city):

        with testit.step(f'Установить адрес в модальном окне "{address_city}"'):
            Select(cls._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY).ajax_option(address_city)
            Select(f'{cls._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_CITY}/following::div[1]').ajax_option(f"Город {address_city}")

    @classmethod
    def set_modal_address_street(cls, street_name: str):
        with testit.step(f'Установить улицу в модальном окне: {street_name}'):
            Select(cls._LOCATOR_SELECT_AJAX_MODAL_ADDRESS_STREET).ajax_option(street_name)

    @classmethod
    def set_modal_address_house(cls, house_name: str):
        with testit.step(f'Установить дом в модальном окне: {house_name}'):
            Locator(f'{cls._LOCATOR_SELECT_MODAL_ADDRESS_LIST_UNCHECKED}//option[contains(text(), "{house_name}")]').click()

            Locator(cls._LOCATOR_BUTTON_MODAL_ADDRESS_ADD_ADDRESS).click()
            Locator(cls._LOCATOR_BUTTON_MODAL_ADDRESS_CONFIRM_ADDRESS).click()

    @classmethod
    def open_modal_address(cls):
        with testit.step(f'Открыть модальное окно'):
            Locator(cls._LOCATOR_BUTTON_OPEN_MODAL_ADD_OBJECT_SMR).click()

    @classmethod
    def add_address(cls, city_name, street_name, house):
        with testit.step(f'Установить адрес "{city_name}", "{street_name}" and "{house}"'):
            cls.open_modal_address()
            cls.set_modal_address_city(address_city=city_name)
            cls.set_modal_address_street(street_name=street_name)
            cls.set_modal_address_house(house_name=house)

    @classmethod
    def enter_dh_for_address(cls, dh_count):
        with testit.step(f'Установить количество ДХ "{dh_count}"'):
            Locator(cls._LOCATOR_TABLE_SERVICES_OPEN_DH).click()
            Input(cls._LOCATOR_TABLE_SERVICES_ENTER_DH).input(f'{dh_count}\n')

    @classmethod
    def set_random_service_key(cls):
        with testit.step('Установить рандомный сервисный ключ', 'Сервисный ключ установлен'):
            Locator(cls._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
            Locator(cls._LOCATOR_CHECKBOX_MODAL_SERVICES_LIST).click()
            Locator(cls._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    @classmethod
    def set_service_key(cls, service_name: str):
        with testit.step(f'Установить услугу "{service_name}"'):
            Locator(cls._LOCATOR_TABLE_SERVICES_OPEN_MODAL_SERVICES).click()
            selector = f'{cls._LOCATOR_CHECKBOX_MODAL_SERVICES_LIST}/parent::div[contains(string(), "{service_name}")]/input'
            Locator(selector).click()
            Locator(cls._LOCATOR_BUTTON_MODAL_SERVICES_SUBMIT).click()

    @classmethod
    def enter_create_project(cls):
        with testit.step('Кликнуть кнопку проект', 'Проект создан'):
            Locator(cls._LOCATOR_BUTTON_CREATE_PROJECT).click()

    @classmethod
    def create_project(cls, project: Project, address=Address, is_prepared: bool = False):
        with testit.step('Создать проект', 'Проект создан'):
            if is_prepared:
                cls.enter_project_name(project.project_name)
                cls.enter_create_project()
            else:
                cls.selected_rf(project.rf)
                cls.selected_is_need_broad(project.is_need_broad)
                cls.selected_type_construct(project.is_type_construct)
                cls.selected_customer_by_inn(project.customer_inn)
                cls.enter_project_name(project.project_name)
                cls.add_address(address.city, address.street, address.house_name)
                cls.enter_dh_for_address(project.dh)
                cls.set_service_key(project.service_key)
                cls.enter_create_project()
