import time
from page import Page
from locator import Locator, Input, CheckBox, Select


class FormB2BMapCreatePreTEOAndTEOOnMap(Page):

    name = 'Создание ТЭО/предТЭО на карте'

    _LOCATOR_MAP = '//div[@class="yandex-common-map"]'
    _LOCATOR_BTN_MAP_FULL_WINDOW = '//ymaps[@class="ymaps-2-1-79-float-button-icon ymaps-2-1-79-float-button-icon_icon_expand"]'
    _LOCATOR_SELECT_MAP_PARENT_OT = '//select[@name="reference_point_id"]'
    _LOCATOR_SELECT_MAP_TECHNOLOGY_TYPE = '//select[@name="link_type_id"]'
    _LOCATOR_BTN_MAP_START_CABLING = '//button[contains(., "Начать прокладку")]'
    _LOCATOR_BTN_MAP_DELETE_PRE_SALE = '//ymaps[@title=" Удалить данные ПредТЭО "]'
    _LOCATOR_BTN_SAVE_IN_MO = '//ymaps[contains(@title, "Сохранить в ТЭО на МО")]'
    _MODAL_CONFIRM = '//form[@data-map-element-action="reloadAfterSave"]'
    _LOCATOR_TEXT_AREA_MODAL_COMMENT = f'{_MODAL_CONFIRM}//textarea'
    _LOCATOR_BTN_CONFIRM_SAVE = f'{_MODAL_CONFIRM}//button[@type="submit"]'


    @classmethod
    def _check_delete_pre_teo(cls) -> bool:
        return Locator(cls._LOCATOR_BTN_MAP_DELETE_PRE_SALE).is_on_page()


    @classmethod
    def _set_coordinate(cls, x: int, y: int):
        pass #найти метод по работе с координатами

    @classmethod
    def _set_full_window(cls):
        Locator(cls._LOCATOR_BTN_MAP_FULL_WINDOW).click()

    @classmethod
    def _set_parent_ot(cls, parent_ot_name: str):
        Select(cls._LOCATOR_SELECT_MAP_PARENT_OT).option(parent_ot_name)


    @classmethod
    def _set_technology_connect(cls, technology_type: str):
        Locator(f'{cls._LOCATOR_SELECT_MAP_TECHNOLOGY_TYPE}//option[text()="{technology_type}"]').click()

    @classmethod
    def _click_start_cabling(cls):
        Locator(cls._LOCATOR_BTN_MAP_START_CABLING).click()


    @classmethod
    def _click_delete_pre_teo(cls):
        Locator(cls._LOCATOR_BTN_MAP_DELETE_PRE_SALE).click()

    @classmethod
    def _click_save_in_mo(cls):
        Locator(cls._LOCATOR_BTN_SAVE_IN_MO).click()

    @classmethod
    def _set_comment(cls, comment: str):
        Input(cls._LOCATOR_TEXT_AREA_MODAL_COMMENT).input(comment)

    @classmethod
    def _confirm_save(cls):
        Locator(cls._LOCATOR_BTN_CONFIRM_SAVE).click()

    @classmethod
    def create_pre_teo_and_teo(cls):

        if cls._check_delete_pre_teo():
            cls._click_delete_pre_teo()
        cls._set_coordinate(200, 400)
        cls._set_technology_connect('xPON')
        cls._click_start_cabling()

        CableModal.set_cable_params(by_client_area=False, cable_type='Проектный_12', cable_line_type='Телефонная канализация', len_cable=100, mr_right='Оптическая муфта')
        CableModal.set_cable_params(by_client_area=True, cable_type='Проектный_12', cable_line_type='Телефонная канализация', len_cable=100, mr_right='Оптическая муфта')

        cls._click_save_in_mo()
        cls._set_comment('Удачное сохранение комментария')
        cls._confirm_save()


class CableModal(Page):
    _LOCATOR_SELECT_MAP_CABLE_LINE_TYPE = '//select[@name="cabling_type_id"]'
    _LOCATOR_SELECT_MAP_CABLE_TYPE = '//select[@name="cable_type_id"]'
    _LOCATOR_INPUT_MAP_CABLE_LEN = '//input[@name="CABLE_LEN"]'
    _LOCATOR_SELECT_MF_RIGHT = '//select[@name="mf_right"]'
    _LOCATOR_BTN_SAVE_PROJECT = '//button[contains(@form, "btn-Projected-Save")]'
    _LOCATOR_BTN_SAVE_AND_CONNECT_CLIENT = '//div[@class="tab-pane active"]//button[@name="saveAndBind"]'
    _LOCATOR_BTN_SAVE_BY_CLIENT = '//div[@class="tab-pane active"]//button[contains(@form, "btn-Projected-Save")]'


    @classmethod
    def _set_cable_line_type(cls, cable_line_type_name: str):
        Select(cls._LOCATOR_SELECT_MAP_CABLE_LINE_TYPE).option(cable_line_type_name)

    @classmethod
    def _set_cable_type(cls, cable_type_name: str):
        Select(cls._LOCATOR_SELECT_MAP_CABLE_TYPE).option(cable_type_name)


    @classmethod
    def _set_cable_len(cls, cable_len: int):
        Input(cls._LOCATOR_INPUT_MAP_CABLE_LEN).input(str(cable_len))


    @classmethod
    def _set_mf_right(cls, mf_name: str):
        Select(cls._LOCATOR_SELECT_MF_RIGHT).option(mf_name)

    @classmethod
    def _click_save_cable_parameters_and_connect_client(cls):
        Locator(cls._LOCATOR_BTN_SAVE_AND_CONNECT_CLIENT).click()


    @classmethod
    def _click_save_cable_parameters_by_client(cls):
        Locator(cls._LOCATOR_BTN_SAVE_BY_CLIENT).click()


    @classmethod
    def set_cable_params(cls, by_client_area: bool, cable_line_type: str, cable_type: str, mr_right: str,
                         len_cable: int):
        cls._set_cable_line_type(cable_line_type)
        cls._set_cable_type(cable_type)
        cls._set_cable_len(len_cable)
        cls._set_mf_right(mr_right)
        if by_client_area:
            cls._click_save_cable_parameters_by_client()
        else:
            cls._click_save_cable_parameters_and_connect_client()
