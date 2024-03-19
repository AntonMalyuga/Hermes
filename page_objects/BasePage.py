import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


class BasePage:
    _LOADER = (By.CSS_SELECTOR, '.h-loader:not(.h-loader--show-loader)')
    _CURRENT_TAB = (By.XPATH, '//a[@aria-expanded="true"]/button')

    def __init__(self, driver: object):
        self._driver = driver

    def close(self):
        self.check_loader()
        try:
            element = self.find_element(self._CURRENT_TAB)
            element.click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click()", element)

    def check_loader(self):
        WebDriverWait(self._driver, 120).until(
            EC.presence_of_element_located(locator=self._LOADER),
            message=f"Не дождался загрузки обновления страницы")
        time.sleep(2)

        return WebDriverWait(self._driver, 120).until(
            EC.presence_of_element_located(locator=self._LOADER),
            message=f"Не дождался загрузки обновления страницы")

    def open(self):
        self._driver.get(self.current_url() + self.path)

    def current_url(self) -> str:
        return self._driver.current_url

    def move_to_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def find_element(self, locator: [str, str], second: int = 40) -> 'WebElement':

        return WebDriverWait(self._driver, second).until(
            EC.presence_of_element_located(locator=locator),
            message=f"Не смог найти элемент по CSS {locator[0]} {locator[1]}")

    def find_elements(self, locator: [str, str], second: int = 40) -> 'list[WebElement]':
        return WebDriverWait(self._driver, second).until(
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
