import time

from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class FormB2BMapCreatePreTEOAndTEOOnMap:

    name = 'Создание ТЭО/предТЭО на карте'

    _LOCATOR_MAP = (By.XPATH, '//div[@class="yandex-common-map"]')
    _LOCATOR_BTN_MAP_FULL_WINDOW = (
        By.XPATH, '//ymaps[@class="ymaps-2-1-79-float-button-icon ymaps-2-1-79-float-button-icon_icon_expand"]')
    _LOCATOR_SELECT_MAP_PARENT_OT = (By.XPATH, '//select[@name="reference_point_id"]')
    _LOCATOR_SELECT_MAP_TECHNOLOGY_TYPE = (By.XPATH, '//select[@name="link_type_id"]')
    _LOCATOR_BTN_MAP_START_CABLING = (By.XPATH, '//button[contains(., "Начать прокладку")]')
    _LOCATOR_BTN_MAP_DELETE_PRE_SALE = (By.XPATH, '//ymaps[@title=" Удалить данные ПредТЭО "]')
    _LOCATOR_BTN_SAVE_IN_MO = (By.XPATH, '//ymaps[contains(@title, "Сохранить в ТЭО на МО")]')
    _MODAL_CONFIRM = '//form[@data-map-element-action="reloadAfterSave"]'
    _LOCATOR_TEXT_AREA_MODAL_COMMENT = (By.XPATH, f'{_MODAL_CONFIRM}//textarea')
    _LOCATOR_BTN_CONFIRM_SAVE = (By.XPATH, f'{_MODAL_CONFIRM}//button[@type="submit"]')

    def _check_delete_pre_teo(self) -> bool:
        try:
            return self.find_element(self._LOCATOR_BTN_MAP_DELETE_PRE_SALE, second=2).is_displayed()
        except ElementNotInteractableException:
            return False

    def _set_coordinate(self, x: int, y: int):
        ActionChains(self._driver).move_by_offset(x, y).click().perform()

    def _set_full_window(self):
        self.find_element(self._LOCATOR_BTN_MAP_FULL_WINDOW).click()

    def _set_parent_ot(self, parent_ot_name: str):
        self.selected_element_by_value(locator=self._LOCATOR_SELECT_MAP_PARENT_OT, value=parent_ot_name)

    def _set_technology_connect(self, technology_type: str):
        ot_locator = (By.XPATH, f'{self._LOCATOR_SELECT_MAP_TECHNOLOGY_TYPE[1]}//option[text()="{technology_type}"]')
        self.find_element(locator=ot_locator).click()

    def _click_start_cabling(self):
        self.find_element(self._LOCATOR_BTN_MAP_START_CABLING).click()

    def _click_delete_pre_teo(self):
        self.find_element(self._LOCATOR_BTN_MAP_DELETE_PRE_SALE).click()

        self._driver.switch_to.alert.accept()

    def _click_save_in_mo(self):
        self.find_element(self._LOCATOR_BTN_SAVE_IN_MO).click()

    def _set_comment(self, comment: str):
        self.find_element(self._LOCATOR_TEXT_AREA_MODAL_COMMENT).send_keys(comment)

    def _confirm_save(self):
        self.find_element(self._LOCATOR_BTN_CONFIRM_SAVE).click()

    def create_pre_teo_and_teo(self):

        if self._check_delete_pre_teo():
            self._click_delete_pre_teo()
        time.sleep(2)
        self._set_coordinate(200, 400)
        time.sleep(2)
        self._set_technology_connect('xPON')
        self._click_start_cabling()

        time.sleep(2)
        CableModal(self._driver).set_cable_params(by_client_area=False, cable_type='Проектный_12', cable_line_type='Телефонная канализация', len_cable=100, mr_right='Оптическая муфта')
        time.sleep(3)
        CableModal(self._driver).set_cable_params(by_client_area=True, cable_type='Проектный_12', cable_line_type='Телефонная канализация', len_cable=100, mr_right='Оптическая муфта')
        time.sleep(2)
        self._click_save_in_mo()
        self._set_comment('Удачное сохранение комментария')
        self._confirm_save()
        time.sleep(5)
        self.check_loader()


class CableModal:
    _LOCATOR_SELECT_MAP_CABLE_LINE_TYPE = (By.XPATH, '//select[@name="cabling_type_id"]')
    _LOCATOR_SELECT_MAP_CABLE_TYPE = (By.XPATH, '//select[@name="cable_type_id"]')
    _LOCATOR_INPUT_MAP_CABLE_LEN = (By.XPATH, '//input[@name="CABLE_LEN"]')
    _LOCATOR_SELECT_MF_RIGHT = (By.XPATH, '//select[@name="mf_right"]')
    _LOCATOR_BTN_SAVE_PROJECT = (By.XPATH, '//button[contains(@form, "btn-Projected-Save")]')
    _LOCATOR_BTN_SAVE_AND_CONNECT_CLIENT = (By.XPATH, '//div[@class="tab-pane active"]//button[@name="saveAndBind"]')
    _LOCATOR_BTN_SAVE_BY_CLIENT = (
    By.XPATH, '//div[@class="tab-pane active"]//button[contains(@form, "btn-Projected-Save")]')

    def _set_cable_line_type(self, cable_line_type_name: str):
        select_element = self.find_element(self._LOCATOR_SELECT_MAP_CABLE_LINE_TYPE)
        select_element.click()
        time.sleep(1)
        Select(select_element).select_by_visible_text(text=cable_line_type_name)

    def _set_cable_type(self, cable_type_name: str):
        select_element = self.find_element(self._LOCATOR_SELECT_MAP_CABLE_TYPE)
        select_element.click()
        time.sleep(1)
        Select(select_element).select_by_visible_text(text=cable_type_name)

    def _set_cable_len(self, cable_len: int):
        self.find_element(self._LOCATOR_INPUT_MAP_CABLE_LEN).send_keys(Keys.CONTROL, 'a')
        self.find_element(self._LOCATOR_INPUT_MAP_CABLE_LEN).send_keys(Keys.BACKSPACE)
        self.find_element(self._LOCATOR_INPUT_MAP_CABLE_LEN).send_keys(cable_len)

    def _set_mf_right(self, mf_name: str):
        select_element = self.find_element(self._LOCATOR_SELECT_MF_RIGHT)
        select_element.click()
        time.sleep(1)
        Select(select_element).select_by_visible_text(text=mf_name)

    def _click_save_cable_parameters_and_connect_client(self):
        self.find_element(self._LOCATOR_BTN_SAVE_AND_CONNECT_CLIENT).click()

    def _click_save_cable_parameters_by_client(self):
        self.find_element(self._LOCATOR_BTN_SAVE_BY_CLIENT).click()

    def set_cable_params(self, by_client_area: bool, cable_line_type: str, cable_type: str, mr_right: str,
                         len_cable: int):
        self._set_cable_line_type(cable_line_type)
        time.sleep(3)
        self._set_cable_type(cable_type)
        self._set_cable_len(len_cable)
        time.sleep(3)
        self._set_mf_right(mr_right)
        if by_client_area:
            self._click_save_cable_parameters_by_client()
        else:
            self._click_save_cable_parameters_and_connect_client()
