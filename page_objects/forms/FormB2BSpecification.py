import time
import testit
from dataclasses import dataclass
from page import Page
from locator import Locator, Select, Input, CheckBox, Radio


@dataclass
class ConstructionMethod:
    contractor: str = 'Подрядный способ'
    gph: str = 'ГПХ'
    hoz: str = 'Хоз. способ'
    smu: str = 'СМУ'
    without_install: str = 'Без установки. Требуется только закупить'


@dataclass
class Specification:
    name: str
    construction_method: str | None = None
    type: str | None = None
    unit: str | None = None
    cnt: int | None = None
    fact_price: float | None = None
    is_new: bool | None = None
    is_imported: bool | None = None
    cnt_port_spd: int | None = None
    cnt_port_tlf: int | None = None
    type_purchase: str | None = None
    type_delivery: str | None = None


class FormB2BSpecification(Page):
    name = 'Редактировать спецификацию оборудования B2C'
    path = 'aggregator/specification/'

    _LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION = '//button[@id="addEquipment"]'
    _LOCATOR_SHOW_MODAL_SPECIFICATION_LIST = '//button[contains(text(), "Показать список оборудования")]'
    _LOCATOR_TABLE_INSERT_SPECIFICATION = '//div[@id="specification-equipment-list"]/table'
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = '//select[contains(@name, "type_installation")]'
    _LOCATOR_BUTTON_MODAL_ADD_SPECIFICATION = '//button[contains(text(),"Добавить выбранные позиции")]'
    _LOCATOR_BUTTON_MODAL_CLOSE = '//button[contains(text(),"Закрыть")]'
    _LOCATOR_BUTTON_CREATE_SPECIFICATION = '//form[@id[contains(., "specification")]]/button[contains(., "Создать спецификацию")]'
    _LOCATOR_BUTTON_SAVE_SPECIFICATION = '//form[@id[contains(., "specification")]]/button[contains(., "Сохранить")]'
    _LOCATOR_BUTTON_DELETE_SPECIFICATION = '//button[contains(text(), "Удалить спецификацию")]'

    @classmethod
    def open_form_by_order(cls, order_id: int):
        with testit.step(f'Открыть форму {cls.name} по заявке {order_id}'):
            cls.open_with_path(f'{cls.path}{order_id}')

    @classmethod
    def delete_specification(cls):
        with testit.step('Удалить спецификацию'):
            if len(Locator(cls._LOCATOR_BUTTON_DELETE_SPECIFICATION).all) != 0:
                Locator(cls._LOCATOR_BUTTON_DELETE_SPECIFICATION).click()

    @classmethod
    def set_construct_method_by_specification_name(cls, specification: Specification):
        with testit.step(
                f'Установить метод строительства "{specification.construction_method}" в спецификации {specification.name}'):
            selector = f'//tr[./td[contains(text(), "{specification.name}")]]//select[contains(@name, "type_installation")]'
            Select(selector).option(specification.construction_method)

    @classmethod
    def set_fact_price_by_specification_name(cls, specification: Specification):
        with testit.step(
                f'Установить фактическую цену "{specification.fact_price}" в спецификации {specification.name}'):
            selector = f'//tr[./td[contains(text(), "{specification.name}")]]//input[contains(@name, "fact_price")]'
            Input(selector).input(str(specification.fact_price))

    @classmethod
    def set_cnt_by_specification_name(cls, specification: Specification):
        with testit.step(
                f'Установить количество "{specification.cnt}" в спецификации {specification.name}'):
            selector = f'//tr[./td[contains(text(), "{specification.name}")]]//input[contains(@name, "quantity")]'
            Input(selector).input(str(specification.cnt))


    @classmethod
    def set_type_purchase_by_specification_name(cls, specification: Specification):
        with testit.step(
                f'Установить закупку "{specification.type_purchase}" в спецификации {specification.name}'):
            selector = f'//tr[./td[contains(text(), "{specification.name}")]]//td[22]//input[contains(text(), "{specification.type_purchase}")]'
            Radio(selector).checked()

    @classmethod
    def open_modal(cls):
        with testit.step('Открыть модальное окно в спецификации'):
            Locator(cls._LOCATOR_BUTTON_OPEN_MODAL_ADD_SPECIFICATION).click()

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
        with testit.step(f'Установить метод строительства "{specification}" в спецификации'):
            specification_locator = f'//tr[@class="specification-new-equipment"]//td[contains(., "{specification}")]/following::td[11]/select[@name[contains(., "type_installation")]]'
            Select(specification_locator).ajax_option(str(specification.construction_method))

    @classmethod
    def create_or_save_specification(cls):
        with testit.step('Нажать кнопку создания/сохранения спецификации'):
            if len(Locator(cls._LOCATOR_BUTTON_CREATE_SPECIFICATION).all) == 0:
                Locator(cls._LOCATOR_BUTTON_SAVE_SPECIFICATION).click()
            else:
                Locator(cls._LOCATOR_BUTTON_CREATE_SPECIFICATION).click()

    @classmethod
    def get_cnt_add_specifications(cls) -> int:
        selector_add_specification = '//table[contains(@id, "specification")]//tr[not(@class) and ./td[@class="specification-equipment-index"]]'
        return len(Locator(selector_add_specification).all)


    @classmethod
    def get_all_add_specifications(cls) -> list[Specification]:
        cnt_specifications = len(Locator(
            '//table[contains(@id, "specification")]//tr[not(@class) and ./td[@class="specification-equipment-index"]]').all)

        specifications = []

        for i in range(cnt_specifications):
            specifications.append(cls._get_add_specification(xpath_position=i + 1))

        return specifications


    @classmethod
    def _get_add_specification(cls, xpath_position: int):
        selector_add_specification = '//table[contains(@id, "specification")]//tr[not(@class) and ./td[@class="specification-equipment-index"]]'
        return Specification(
            name=Locator(f'{selector_add_specification}[{xpath_position}]//td[7]').text,
            construction_method=Locator(
                f'{selector_add_specification}[{xpath_position}]//td[17]//option[@selected]').text,
            type=Locator(f'{selector_add_specification}[{xpath_position}]//td[6]').text,
            unit=Locator(f'{selector_add_specification}[{xpath_position}]//td[8]').text,
            cnt=int(Locator(f'{selector_add_specification}[{xpath_position}]//td[9]/input').get_attribute('value')),
            fact_price=float(Locator(f'{selector_add_specification}[{xpath_position}]//td[14]/input').get_attribute('value')),
            is_new=Radio(f'{selector_add_specification}[{xpath_position}]//td[15]/input').is_checked(),
            is_imported=Radio(f'{selector_add_specification}[{xpath_position}]//td[16]/input').is_checked(),
            cnt_port_spd=int(Locator(f'{selector_add_specification}[{xpath_position}]//td[20]/input').get_attribute('value')),
            cnt_port_tlf=int(Locator(f'{selector_add_specification}[{xpath_position}]//td[21]/input').get_attribute('value')),
            type_purchase=Locator(
                f'{selector_add_specification}[{xpath_position}]//td[22]//input[@checked]').text.strip(),
            type_delivery=Locator(
                f'{selector_add_specification}[{xpath_position}]//td[23]//input[@checked]').text.strip()
        )

    @classmethod
    def get_cnt_html_th_table(cls):
        return len(Locator('//table[contains(@id, "specification")]//tr/th').all) - 1

    @classmethod
    def get_cnt_html_td_by_first_add_specification(cls):
        return len(Locator('//table[contains(@id, "specification")]//tr[not(@class) and ./td[@class="specification-equipment-index"]]/td').all)

    @classmethod
    def get_cnt_html_td_by_first_new_specification(cls):
        return len(Locator('//table[contains(@id, "specification")]//tr[@class="specification-new-equipment" and @style]/td').all)

    @classmethod
    def add_specification(cls, specification: Specification):
        with testit.step('Добавить спецификацию', 'Спецификация сохранена'):
            cls.open_modal()
            cls.show_specification_list_by_modal()
            cls.add_specification_by_modal(specification.name)
            cls.set_construct_method_by_specification_name(specification)
            cls.create_or_save_specification()

