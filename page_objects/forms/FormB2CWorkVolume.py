import time
import testit

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class B2cFormWorkVolume(BasePage):

    name = 'Редактировать объемы ПИР/СМР B2C'

    _LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK = (By.CSS_SELECTOR, 'button[data-target^="#add-work-modal"]')
    _LOCATOR_TABLE_OPEN_MODAL_ADD_WORK = (By.XPATH, '//tbody[@id="add-work-table-tbody"]')
    _LOCATOR_CHECK_OPEN_MODAL = (By.CSS_SELECTOR, '.modal.fade.in')
    _LOCATOR_BUTTON_MODAL_ADD_WORK = (By.XPATH, '//div[@class="modal-content"]//button[text()="Добавить"]')
    _LOCATOR_TABLE_INSERT_WORKS = (By.XPATH, '//table[contains(@class, "hook--work-table")]')
    _LOCATOR_BUTTON_SAVE_WORKS = (By.CSS_SELECTOR, 'button.btn.btn-primary.js--validation-hidden-forms')
    _LOCATOR_LABEL_CONSTRUCTION_METHOD = (By.XPATH, '//label[@class="radio-inline"')

    def check_open_modal(self):
        with testit.step('Открыть модальное окно', 'Окно открыто'):
            time.sleep(2)
            return self.find_element(self._LOCATOR_CHECK_OPEN_MODAL)

    def add_works(self, works: dict):
        with testit.step(f'Добавить работы "{works}"'):
            self.check_loader()
            self.find_element(locator=self._LOCATOR_BUTTON_OPEN_MODAL_ADD_WORK).click()
            self.check_open_modal()

        if 'works_keys' in works:
            self.add_works_by_modal(works['works_keys'])
            self.set_works_value(works['works_keys'])
            self.set_natural_indicators(works['works_keys'])

        if 'works_core' in works:
            self.add_works_by_modal(works['works_core'])
            self.set_works_value(works['works_core'])
            self.set_method_by_core(works['works_core'])
        self.save_works()

    def add_works_by_modal(self, works: dict):
        with testit.step(f'Добавить работы в модальном окне "{works}"'):
            for work, work_params in works.items():
                self.find_element((By.XPATH,
                                   f'{self._LOCATOR_TABLE_OPEN_MODAL_ADD_WORK[1]}//td[contains(text(),"{work_params["type"]}: {work}")]/ancestor::tr[1]')).click()

        self.find_element(self._LOCATOR_BUTTON_MODAL_ADD_WORK).click()

    def set_construct_method(self, type_construct):
        with testit.step(f'Установить метод строительства "{type_construct}"'):
            self.find_element((By.XPATH,
                               f'{self._LOCATOR_LABEL_CONSTRUCTION_METHOD[1]} and contains(.,"{type_construct}")]/input')).click()

    def set_works_value(self, works: dict):
        with testit.step(f'Добавить значения работ "{works}"'):
            for work, work_params in works.items():
                time.sleep(1)
                work_locator = f'//tr[@data-work-name[contains(., "{work}")] and @data-work-type="{work_params["type"]}"]//input[@class="form-control input-sm volumes-form-work-quantity-input"]'
                self.find_element((By.XPATH, work_locator)).send_keys(Keys.CONTROL, 'a')
                self.find_element((By.XPATH, work_locator)).send_keys(Keys.BACKSPACE)
                self.find_element((By.XPATH, work_locator)).send_keys(int(work_params["qty"]))

    def set_method_by_core(self, works: dict):
        with testit.step(f'Установить тип строительства по услуге Core "{works}"'):
            for work, work_params in works.items():
                time.sleep(1)
                work_locator = f'//tr[@data-work-name[contains(., "{work}")] and @data-work-type="{work_params["type"]}"]//select[@class="form-control input-sm core-construction-method-selector"]'
                self.selected_element_by_value(locator=(By.XPATH, work_locator), value=work_params["method"])

    def set_natural_indicators(self, works: dict):
        with testit.step(f'Установить натуральные показатели "{works}"'):
            for work, work_params in works.items():
                time.sleep(1)
                work_locator = f'//tr[@data-work-name[contains(., "{work}")] and @data-work-type="{work_params["type"]}"]//select[@class="form-control input-sm inputOrText "]'
                self.selected_element_by_value(locator=(By.XPATH, work_locator), value=work_params["natural_indicator"])

    def save_works(self):
        with testit.step(f'Сохранить работы', 'Работы сохранены'):
            self.find_element(self._LOCATOR_BUTTON_SAVE_WORKS).click()
