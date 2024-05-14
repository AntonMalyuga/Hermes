import time
import testit
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


class BasePage:
    _LOADER = (By.CSS_SELECTOR, '.h-loader:not(.h-loader--show-loader)')
    _CURRENT_TAB = (By.XPATH, '//a[@aria-expanded="true"]/button')
    _LOCATOR_RELOAD_ORDER = (By.XPATH, '//a[@title="Обновить"]')
    _NOT_CURRENT_TAB = (By.XPATH, '//a[@aria-expanded="false"]//button')
    _LOCATOR_ODER_CURRENT_STAGE = (
        By.CSS_SELECTOR, '.panel.panel-small-margin div.panel-body .agg-value:nth-child(3) .agg-key-value__value')
    _ALERT = (By.XPATH, '//div[@class="toast-message"]')

    def __init__(self, driver: webdriver):
        self._driver = driver

    def check_alert(self):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException)
            alert = WebDriverWait(self._driver, timeout=0, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_all_elements_located(locator=self._ALERT))
            if len(alert) != 0:
                raise f'Получена ошибка в приложении: {alert[0].text}'
        except Exception:
            return True

    def __get_current_stage(self) -> str:
        return str(self.find_element(locator=self._LOCATOR_ODER_CURRENT_STAGE).get_property(
            'innerText')).translate({ord('«'): None, ord('»'): None})

    def close(self):
        time.sleep(3)
        self.check_loader()
        element = self.find_element(self._CURRENT_TAB)

        try:
            element.click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click()", element)

    def delete_text_by_js(self, element):
        self._driver.execute_script("arguments[0].removeAttribute('value')", element)

    def check_loader(self, cnt_check: int = 0):
        if cnt_check > 20:
            raise Exception('Превышено количество ожиданий обновления страницы')

        if len(self.find_elements(self._LOADER)) == 0:
            time.sleep(2)
            cnt_check += 1
            self.check_loader(cnt_check)
        else:
            time.sleep(2)
            return True

    def check_current_stage(self, stage_name: str, second_do_reload: int = 10):
        if self.__get_current_stage().find(str(stage_name)) != -1:
            return True

        self.try_reload_page(stage_name=stage_name, second_do_reload=second_do_reload)

    def try_reload_page(self, stage_name: str, second_do_reload: int, try_reload: int = 0, max_reload: int = 5):
        if try_reload < max_reload:
            self.check_loader()
            self.reload_order()
            time.sleep(second_do_reload)
            self.check_loader()

            if self.__get_current_stage().find(str(stage_name)) != -1:
                return True

            try_reload += 1
            self.try_reload_page(stage_name=stage_name, second_do_reload=second_do_reload, try_reload=try_reload)
        else:
            raise Exception(f'Некорректный этап, ожидаемый "{stage_name}", полученный "{self.__get_current_stage()}"')

    def reload_order(self):
        self.find_element(self._LOCATOR_RELOAD_ORDER).click()

    def open(self):
        url = f'{self.current_url()}{self.path}'
        self._driver.get(url)

    def open_for_link(self, path):
        url = f'{self.__base_url()}{path}'
        self._driver.get(url)

    def open_for_path(self, path):
        url = f'{self.__base_url()}{self.path}{path}'
        self._driver.get(url)

    def current_url(self) -> str:
        current_url = self._driver.current_url
        return self._driver.current_url

    def close_not_current_tab(self):
        self.check_loader()
        tabs = self.find_elements(locator=self._NOT_CURRENT_TAB)
        for tab in tabs:
            tab.click()

    def move_to_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def delete_element(self, locator):
        element = self.find_element(locator)
        self._driver.execute_script('arguments[0].remove()', element)

    def find_element(self, locator: [str, str], second: int = 40) -> 'WebElement':
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        try:
            return WebDriverWait(self._driver, timeout=10, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located(locator=locator))
        except Exception:
            return WebDriverWait(self._driver, timeout=second, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located(locator=locator),
                message=f"Не смог найти элемент по CSS {locator[0]} {locator[1]}")

    def find_elements(self, locator: [str, str], second: int = 40) -> 'list[WebElement]':
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        try:
            return WebDriverWait(self._driver, timeout=10, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_all_elements_located(locator=locator))
        except Exception:
            return WebDriverWait(self._driver, timeout=second, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_all_elements_located(locator=locator),
                message=f"Не смог найти элементы по CSS {locator}")

    def selected_element_by_value(self, locator, value: str):
        def __check_class_names_by_select(select_element, *class_names) -> bool:
            for i in range(len(class_names)):
                if str(select_element.get_attribute('class')).find(class_names[i]) != -1:
                    return True

        select = self.find_element(locator)

        if __check_class_names_by_select(select, 'suggest__hidden'):

            self.find_element((By.CSS_SELECTOR, f'{locator[1]} ~ div')).click()
            time.sleep(2)
            self.find_element((By.CSS_SELECTOR, f'{locator[1]} ~ div .suggest--input-field')).send_keys(value)
            time.sleep(2)
            self.find_element((By.CSS_SELECTOR, f'{locator[1]} ~ div .suggest--option')).click()

        elif __check_class_names_by_select(select, 'form-control input-sm', 'available-values'):

            Select(select).select_by_visible_text(value)

        else:
            raise TypeError(
                f'Тег не имеет соответствующий класс, получен {select.get_attribute("class")}')

    def __base_url(self) -> str:
        return self._driver.base_url
