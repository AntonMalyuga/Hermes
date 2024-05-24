import random

import testit
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class FormB2BWorkVolume:
    name = 'Редактировать объемы ПИР/СМР B2B'

    _LOCATOR_BTN_SHOW_ALL_WORKS = '//button[@title="Отобразить все объемы работ"]')
    _LOCATOR_INPUTS_VALUE_ALL_WORKS = (
        By.XPATH, '//div[@id="works-tab"]//input[contains(@name, "work")]/ancestor::tr[1]')
    _LOCATOR_BTN_SAVE_WORKS = '//form[contains(@id, "volumesForm")]//button[contains(text(), "Сохранить")]')
    _LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED = (
        By.XPATH, '//div[contains(@id,"volumesFormTab")]/div[@class="alert-success alert"]')

    def click_show_all_works(self):
        self.find_element(self._LOCATOR_BTN_SHOW_ALL_WORKS).click()

    def get_all_works(self) -> list[WebElement]:
        return self.find_elements(self._LOCATOR_INPUTS_VALUE_ALL_WORKS)

    def set_random_value_for_works(self):
        works = self.get_all_works()
        random_work_position = random.randrange(0, stop=len(works))
        random_value = int(random.randrange(1, 10))
        code_work = works[random_work_position].get_attribute('title')
        with testit.step(f'Установить работу по id {code_work} со значением {random_value}'):
            works[random_work_position].find_element(by=By.CSS_SELECTOR, value='input').send_keys(random_value)

    def save_works(self):
        self.find_element(self._LOCATOR_BTN_SAVE_WORKS).click()

    def delete_alert(self):
        self.delete_element(self._LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED)

    def check_save_changes(self):
        if self.find_element(self._LOCATOR_DIV_ALERT_CHANGE_WORK_COMPLETED).is_enabled():
            return True
        else:
            raise Exception('Работы не изменены')

    def fill_and_save_random_works(self):
        self.check_loader()
        self.delete_alert()
        self.click_show_all_works()
        self.set_random_value_for_works()
        self.save_works()
        self.check_save_changes()
        self.check_alert()

        self.close()
