from dataclasses import dataclass
import testit
import math
from locator import Locator, Input, Select
from page import Page


@dataclass
class ClusterMethods:
    change_line_type: str | None = None
    change_cable_type: str | None = None
    change_line_length: int | None = None
    change_create_cable_chanel: int | None = None
    change_gnb_group_1_3: int | None = None
    change_gnb_group_4_6: int | None = None
    change_installation_of_wooden_supports: int | None = None
    change_installation_of_reinforced_concrete_supports: int | None = None
    change_installation_of_metal_supports: int | None = None
    change_change_support_type: int | None = None
    change_cable_entry_device: int | None = None
    change_insert_cable_channel: int | None = None
    change_recovery_cable_channel: int | None = None
    change_well_installation: int | None = None


@dataclass
class Work:
    name: str
    work_type: str
    count: int


@dataclass
class HtmlWork:
    name: str
    code_r12: str
    type: str
    price_without_nds: float
    unit: str
    cnt: int
    cost_without_nds: float


@dataclass
class HtmlWorkCluster:
    cable_name: str | None
    address: str | None
    order: int | None
    type_line: str | None
    cable_type: str | None
    line_length: int | None
    create_cable_chanel: int | None
    gnb_group_1_3: int | None
    gnb_group_4_6: int | None
    installation_of_wooden_supports: int | None
    installation_of_reinforced_concrete_supports: int | None
    installation_of_metal_supports: int | None
    change_support_type: int | None
    cable_entry_device: int | None
    insert_cable_channel: int | None
    recovery_cable_channel: int | None
    well_installation: int | None


class FormB2BWorkVolume(Page):
    name = 'Редактировать объемы ПИР/СМР B2B'
    path = '/aggregator/volumes/'

    _LOCATOR_BTN_SHOW_ALL_WORKS = '//button[@title="Отобразить все объемы работ"]'
    _LOCATOR_INPUTS_VALUE_ALL_WORKS = '//div[@id="works-tab"]//tbody//tr[not(@class="hidden") and @data-work-type]'
    _LOCATOR_BTN_SAVE_WORKS = '//form[contains(@id, "volumesForm")]//button[contains(text(), "Сохранить")]'
    _LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED = '//div[contains(@id,"volumesFormTab")]/div[@class="alert-success alert"]'
    _LOCATOR_BTN_DELETE_WORKS = '//tr[not(@class="hidden")]//button'
    _LOCATOR_SELECT_FRAME_CALCULATOR = '//select[@name = "ebpr_frame_id"]'
    _LOCATOR_BTN_SAFE_FRAME_CALCULATOR = '//button[@id = "changeEbpr"]'
    _LOCATOR_ADD_WORKS = '//table[contains(@class, "work-table")]//tr[not(contains(@class,"hidden")) and @data-work-type]'
    _LOCATOR_TABLE_CLUSTER = '//table[.//div[contains(text(), "Список участков")]]'

    @classmethod
    def open_form(cls, order_id):
        with testit.step(f'Открыть форму редактирования ПИР/СМР по заявке: {order_id}'):
            cls.open_with_path(f'{cls.path}{order_id}')

    @classmethod
    def change_calculator_frame(cls, frame_name: str):
        with testit.step(f'Изменить калькулятор на: {frame_name}'):
            Select(cls._LOCATOR_SELECT_FRAME_CALCULATOR).option(frame_name)
            Locator(cls._LOCATOR_BTN_SAFE_FRAME_CALCULATOR).click()

    @classmethod
    def get_current_name_calculator_frame(cls) -> str:
        with testit.step('Получить текущее имя калькулятора'):
            return Locator(f'{cls._LOCATOR_SELECT_FRAME_CALCULATOR}/option[@selected]').text

    @classmethod
    def get_html_work_cluster_by_index(cls, position_row: int) -> HtmlWorkCluster:

        position_row += 1

        return HtmlWorkCluster(
            cable_name=Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]///td[1]').text,
            address=Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]///td[2]').text,
            order=int(Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[3]').text),
            type_line=Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[4]//option[@selected]').text,
            cable_type=Locator(
                f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[5]//input').get_attribute('data-title'),
            line_length=int(Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[6]//input').text),
            create_cable_chanel=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[7]//input').text),
            gnb_group_1_3=int(Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[8]//input').text),
            gnb_group_4_6=int(Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[9]//input').text),
            installation_of_wooden_supports=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[10]//input').text),
            installation_of_reinforced_concrete_supports=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[11]//input').text),
            installation_of_metal_supports=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[12]//input').text),
            change_support_type=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[13]//input').text),
            cable_entry_device=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[14]//input').text),
            insert_cable_channel=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[15]//input').text),
            recovery_cable_channel=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[16]//input').text),
            well_installation=int(
                Locator(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[17]//input').text),
        )

    @classmethod
    def get_html_add_works(cls) -> list[HtmlWork]:
        with testit.step('Получить все работы из интерфейса добавления работ'):
            add_works_cnt = Locator(cls._LOCATOR_ADD_WORKS).count

            works = []

            for i in range(add_works_cnt):
                works.append(
                    HtmlWork(
                        name=Locator(
                            f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//div[contains(@class, "work-name")]').text.strip(),
                        code_r12=Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[3]').text.strip(),
                        type=Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[4]').text,
                        price_without_nds=float(
                            Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[5]').text.strip().replace(',', '.')),
                        unit=Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[6]').text,
                        cnt=int(
                            Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[7]//input').get_attribute('value').strip()),
                        cost_without_nds=float(
                            Locator(f'{cls._LOCATOR_ADD_WORKS}[{i + 1}]//td[8]').text.replace(' ', '').replace(',',
                                                                                                               '.'))
                    )
                )

            return works

    @classmethod
    def click_show_all_works(cls):
        with testit.step(f'Нажать на кнопку "Отобразить все работы"'):
            Locator(cls._LOCATOR_BTN_SHOW_ALL_WORKS).click()

    @classmethod
    def get_cnt_visible_works(cls) -> int:
        cnt_works = Locator(cls._LOCATOR_INPUTS_VALUE_ALL_WORKS).count
        with testit.step(f'Посчитать количество отображаемых работ: {cnt_works}'):
            return cnt_works

    @classmethod
    def add_work(cls, work: Work):
        with testit.step(f'Добавить работу {work.name}'):
            selector = f'//tr[@data-work-type="{work.work_type}" and .//div[contains(@data-work-name, "{work.name}")]]//input'
            Input(selector).input(str(work.count))

    @classmethod
    def change_cnt_work_by_add_work(cls, work: Work, new_count: int):
        with testit.step(f'Изменить количество работы {work.name} на {work.count}'):
            Input(
                f'{cls._LOCATOR_ADD_WORKS}[@data-work-type="{work.work_type}" and .//div[contains(@data-work-name, "{work.name}")]]//input').input(
                str(new_count))

    @classmethod
    def add_works(cls, list_works: list[Work]):
        with testit.step(f'Добавить работы из списка {list_works}'):
            for work in list_works:
                cls.add_work(work)

    @classmethod
    def delete_all_works(cls):
        with testit.step(f'Удалить все работы'):
            works = cls.get_cnt_visible_works()
            for work in range(works):
                Locator(cls._LOCATOR_BTN_DELETE_WORKS).click()

    @classmethod
    def save_works(cls):
        with testit.step(f'Нажать на кнопку "Сохранить"'):
            Locator(cls._LOCATOR_BTN_SAVE_WORKS).click()

    @classmethod
    def check_save_changes(cls):
        with testit.step(f'Проверить отрбражение информации о сохранении работ'):
            if Locator(cls._LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED).is_on_page():
                return True
            else:
                raise Exception('Работы не изменены')

    @classmethod
    @testit.step('Добавить рандомные работы и сохранить')
    def fill_and_save_random_works(cls, work: Work):
        cls.click_show_all_works()
        cls.add_work(work)
        cls.save_works()
        cls.check_save_changes()

    @classmethod
    def change_cluster_parameters_by_row(cls, position_row: int, method: ClusterMethods):
        position_row += 1
        cls.__change_line_type(position_row, method.change_line_type)
        cls.__change_cable_type(position_row, method.change_cable_type)
        cls.__change_line_length(position_row, method.change_line_length)
        cls.__change_create_cable_chanel(position_row, method.change_create_cable_chanel)
        cls.__change_gnb_group_1_3(position_row, method.change_gnb_group_1_3)
        cls.__change_gnb_group_4_6(position_row, method.change_gnb_group_4_6)
        cls.__change_installation_of_wooden_supports(position_row, method.change_installation_of_wooden_supports)
        cls.__change_installation_of_reinforced_concrete_supports(position_row,
                                                                  method.change_installation_of_reinforced_concrete_supports)
        cls.__change_installation_of_metal_supports(position_row, method.change_installation_of_metal_supports)
        cls.__change_support_type(position_row, method.change_change_support_type)
        cls.__change_cable_entry_device(position_row, method.change_cable_entry_device)
        cls.__change_insert_cable_channel(position_row, method.change_insert_cable_channel)
        cls.__change_recovery_cable_channel(position_row, method.change_recovery_cable_channel)
        cls.__change_well_installation(position_row, method.change_well_installation)

    @classmethod
    def __change_line_type(cls, position_row: int, value: str):
        if value:
            Select(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[4]//select').option(value)

    @classmethod
    def __change_cable_type(cls, position_row: int, value: str):
        if value:
            Select(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[5]//input').ajax_option(value)

    @classmethod
    def __change_line_length(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[6]//input').input(str(value))

    @classmethod
    def __change_create_cable_chanel(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[7]//input').input(str(value))

    @classmethod
    def __change_gnb_group_1_3(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[8]//input').input(str(value))

    @classmethod
    def __change_gnb_group_4_6(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[9]//input').input(str(value))

    @classmethod
    def __change_installation_of_wooden_supports(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[10]//input').input(str(value))

    @classmethod
    def __change_installation_of_reinforced_concrete_supports(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[11]//input').input(str(value))

    @classmethod
    def __change_installation_of_metal_supports(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[12]//input').input(str(value))

    @classmethod
    def __change_support_type(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[13]//input').input(str(value))

    @classmethod
    def __change_cable_entry_device(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[11]//input').input(str(value))

    @classmethod
    def __change_insert_cable_channel(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[12]//input').input(str(value))

    @classmethod
    def __change_recovery_cable_channel(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[13]//input').input(str(value))

    @classmethod
    def __change_well_installation(cls, position_row: int, value: int):
        if value:
            Input(f'{cls._LOCATOR_TABLE_CLUSTER}/tbody/tr[{position_row}]//td[14]//input').input(str(value))
