import testit
from dataclasses import dataclass, field
from page import Page
from locator import Locator, Select, Input


@dataclass
class Work:
    name: str
    qty: int
    type: str
    natural_indicator: str
    construct_method: str


@dataclass
class Works:
    works_key: list[Work] | None
    works_core: list[Work] | None


class B2cFormWorkVolume(Page):
    name = 'Редактировать объемы ПИР/СМР B2C'

    _LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK = '//button[contains(text(), "Добавить работу")]'
    _LOCATOR_TABLE_OPEN_MODAL_ADD_WORK = '//tbody[@id="add-work-table-tbody"]'
    _LOCATOR_BUTTON_MODAL_ADD_WORK = '//div[@class="modal-content"]//button[text()="Добавить"]'
    _LOCATOR_TABLE_INSERT_WORKS = '//table[contains(@class, "hook--work-table")]'
    _LOCATOR_BUTTON_SAVE_WORKS = '//button[contains(text(), "Сохранить")]'
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = '//label[@class="radio-inline"'

    @classmethod
    def add_works(cls, works: Works):
        with testit.step(f'Добавить работы "{works}"'):
            Locator(cls._LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK).click()

        if works.works_key:
            cls.add_works_by_modal(works.works_key)
            cls.set_works_value(works.works_key)
            cls.set_natural_indicators(works.works_key)

        if works.works_core:
            cls.add_works_by_modal(works.works_core)
            cls.set_works_value(works.works_core)
            cls.set_method_by_core(works.works_core)
        cls.save_works()

    @classmethod
    def add_works_by_modal(cls, works: list[Work]):
        for work in works:
            with testit.step(f'Добавить работу в модальном окне "{work.name}"'):
                Locator(
                    f'{cls._LOCATOR_TABLE_OPEN_MODAL_ADD_WORK}//td[contains(text(),"{work.type}: {work.name}")]/ancestor::tr[1]').click()
        Locator(cls._LOCATOR_BUTTON_MODAL_ADD_WORK).click()

    @classmethod
    def set_construct_method(cls, type_construct):
        with testit.step(f'Установить метод строительства "{type_construct}"'):
            Locator(f'{cls._LOCATOR_LABEL_CONSTRUCTION_METHOD} and contains(.,"{type_construct}")]/input').click()

    @classmethod
    def set_works_value(cls, works: list[Work]):
        for work in works:
            with testit.step(f'Добавить значения {work.qty} для работы "{work.name}"'):
                work_locator = f'//tr[@data-work-name[contains(., "{work.name}")] and @data-work-type="{work.type}"]//input[@class="form-control input-sm volumes-form-work-quantity-input"]'
                Input(work_locator).input(str(work.qty))

    @classmethod
    def set_method_by_core(cls, works: list[Work]):
        for work in works:
            with testit.step(f'Установить тип строительства по услуге Core "{works}"'):
                work_locator = f'//tr[@data-work-name[contains(., "{work.name}")] and @data-work-type="{work.type}"]//select[@class="form-control input-sm core-construction-method-selector"]'
                Select(work_locator).ajax_option(work.construct_method)

    @classmethod
    def set_natural_indicators(cls, works: list[Work]):
        for work in works:
            with testit.step(f'Установить натуральные показатель "{work.natural_indicator}" на работу "{work.name}"'):
                work_locator = f'//tr[@data-work-name[contains(., "{work.name}")] and @data-work-type="{work.type}"]//select[@class="form-control input-sm inputOrText "]'
                Select(work_locator).option(work.natural_indicator)

    @classmethod
    def save_works(cls):
        with testit.step(f'Сохранить работы', 'Работы сохранены'):
            Locator(cls._LOCATOR_BUTTON_SAVE_WORKS).click()
