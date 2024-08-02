import time
import testit
from dataclasses import dataclass
from page import Page
from locator import Locator, Select, Input


@dataclass
class Specification:
    natural_indicator: str
    construct_method: str
    specifications_key: str | None
    specifications_core: str | None


class B2cFormSpecification(Page):
    name = 'Редактировать спецификацию оборудования B2C'

    _LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION = 'button[id="addEquipment"]'
    _LOCATOR_CHECK_OPEN_MODAL = '.modal.fade.in'
    _LOCATOR_SHOW_MODAL_SPECIFICATION_LIST = '//button[@data-url="/b2c/specification/equipment_list"]'
    _LOCATOR_TABLE_INSERT_SPECIFICATION = '//div[@id="specification-equipment-list"]/table'
    _LOCATOR_BUTTON_SAVE_WORKS = 'button.btn.btn-primary.js--validation-hidden-forms'
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = '//label[@class="radio-inline"'
    _LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION = '//button[@class[contains(.,"b2c-specification-add-equipments")]]'
    _LOCATOR_BUTTON_MODAL_CLOSE = '//div[@class[contains(.,"specification-modal-controls")]]/button[@data-dismiss="modal"]'
    _LOCATOR_BUTTON_CREATE_SPECIFICATION = '//form[@id[contains(., "specification")]]/button[contains(., "Создать спецификацию")]'

    @classmethod
    def set_construct_method(cls, type_construct):
        with testit.step(f'Выбрать метод строительства "{type_construct}" с помощью B2C спецификации',
                         'Тип строительства выбран'):
            selector = f'{cls._LOCATOR_LABEL_CONSTRUCTION_METHOD} and contains(.,"{type_construct}")]/input'
            Locator(selector).click()

    @classmethod
    def open_modal(cls):
        with testit.step('Открыть модальное окно в спецификации'):
            element = Locator(cls._LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION).click()

    @classmethod
    def close_modal(cls):
        with testit.step('Закрыть модальное окно', 'Окно закрыто'):
            Locator(cls._LOCATOR_BUTTON_MODAL_CLOSE).click()

    @classmethod
    def confirm_selected_specification(cls):
        with testit.step('Подтвердить выбранную спецификацию'):
            Locator(cls._LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION).click()

    @classmethod
    def show_specification_list_by_modal(cls):
        with testit.step('Показать список спецификаций'):
            Locator(cls._LOCATOR_SHOW_MODAL_SPECIFICATION_LIST).click()

    @classmethod
    def add_specification_by_modal(cls, specifications: str):
        with testit.step(f'Выбрать спецификацию "{specifications}" в модальном окне формы спецификации'):
            Locator(
                f'{cls._LOCATOR_TABLE_INSERT_SPECIFICATION}//td[@data-name="name" and contains(.,"{specifications}")]/ancestor::tr[1]//input').click()
            cls.confirm_selected_specification()
            cls.close_modal()

    @classmethod
    def set_method_by_specification(cls, specification: Specification):
        with testit.step(f'Установить метод строительства "{specification.construct_method}" в спецификации'):
            specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification.construct_method}")]/following::td[11]/select[@name[contains(., "type_installation")]]'
            Select(specification_locator).ajax_option(specification.construct_method)

    @classmethod
    def set_natural_indicators(cls, specification: Specification):
        with testit.step(f'Установить натуральные показатели "{specification}" в спецификации'):
            specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification.specifications_key}")]/following::td[1]/select[@id[contains(., "naturalIndicator")]]'
            Select(specification_locator).ajax_option(specification.natural_indicator)

    @classmethod
    def create_specification(cls):
        with testit.step('Нажать кнопку создания спецификации'):
            Locator(cls._LOCATOR_BUTTON_CREATE_SPECIFICATION).click()

    @classmethod
    def add_specification(cls, specifications: Specification):
        with testit.step('Добавить спецификацию', 'Спецификация сохранена'):
            cls.set_construct_method(specifications.construct_method)
            cls.open_modal()
            cls.show_specification_list_by_modal()

            if 'specifications_keys' in specifications:
                cls.add_specification_by_modal(specifications.specifications_key)
                cls.set_natural_indicators(specifications)
            if 'specifications_core' in specifications:
                cls.add_specification_by_modal(specifications.specifications_core)
                cls.set_method_by_specification(specifications)
            cls.create_specification()
