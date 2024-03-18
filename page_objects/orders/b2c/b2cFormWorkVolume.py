import time

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class B2cFormWorkVolume(BasePage):
    _LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK = (By.CSS_SELECTOR, 'button[data-target^="#add-work-modal"]')
    _LOCATOR_TABLE_OPEN_MODAL_ADD_WORK = (By.XPATH, '//tbody[@id="add-work-table-tbody"]')
    _LOCATOR_CHECK_OPEN_MODAL = (By.CSS_SELECTOR, '.modal.fade.in')
    _LOCATOR_BUTTON_MODAL_ADD_WORK = (By.XPATH, '//div[@class="modal-content"]//button[text()="Добавить"]')
    _LOCATOR_TABLE_INSERT_WORKS = (By.XPATH, '//table[contains(@class, "hook--work-table")]')
    _LOCATOR_BUTTON_SAVE_WORKS = (By.CSS_SELECTOR, 'button.btn.btn-primary.js--validation-hidden-forms')
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = (By.XPATH, '//label[@class="radio-inline"')

    def check_open_modal(self):
        time.sleep(2)
        return self.find_element(self._LOCATOR_CHECK_OPEN_MODAL)

    def add_works(self, works: dict):
        self.check_loader()
        self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK).click()
        self.check_open_modal()

        for work, work_params in works.items():
            self.find_element((By.XPATH,
                               f'{self._LOCATOR_TABLE_OPEN_MODAL_ADD_WORK[1]}//td[contains(text(),"{work_params["type"]}: {work}")]/ancestor::tr[1]')).click()

        self.find_element(self._LOCATOR_BUTTON_MODAL_ADD_WORK).click()

        self.set_works_value(works)
        self.set_natural_indicators(works)
        self.save_works()

    def set_construct_method(self, type_construct):
        self.find_element((By.XPATH,
                           f'{self._LOCATOR_LABEL_CONSTRUCTION_METHOD[1]} and contains(.,"{type_construct}")]/input')).click()

    def set_works_value(self, works: dict):
        for work, work_params in works.items():
            time.sleep(1)
            work_locator = f'//tr[@data-work-name[contains(., "{work}")] and @data-work-type="{work_params["type"]}"]//input[@class="form-control input-sm volumes-form-work-quantity-input"]'
            self.find_element((By.XPATH, work_locator)).send_keys(Keys.CONTROL, 'a')
            self.find_element((By.XPATH, work_locator)).send_keys(Keys.BACKSPACE)
            self.find_element((By.XPATH, work_locator)).send_keys(int(work_params["qty"]))

    def set_natural_indicators(self, works: dict):
        for work, work_params in works.items():
            time.sleep(1)
            work_locator = f'//tr[@data-work-name[contains(., "{work}")] and @data-work-type="{work_params["type"]}"]//select[@class="form-control input-sm inputOrText "]'
            self.selected_element_by_value(locator=(By.XPATH, work_locator), value=work_params["natural_indicator"])

    def save_works(self):
        self.find_element(self._LOCATOR_BUTTON_SAVE_WORKS).click()
