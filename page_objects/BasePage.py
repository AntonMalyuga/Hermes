import time
import testit
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    _LOADER = (By.CSS_SELECTOR, '.h-loader:not(.h-loader--show-loader)')
    _CURRENT_TAB = (By.XPATH, '//a[@aria-expanded="true"]/button')
    _NOT_CURRENT_TAB = (By.XPATH, '//a[@aria-expanded="false"]//button')

    def __init__(self, driver: object):
        self._driver = driver

    @testit.step('Close current tab hermes')
    def close(self):
        self.check_loader()
        try:
            element = self.find_element(self._CURRENT_TAB)
            element.click()
        except ElementClickInterceptedException:
            self._driver.execute_script("arguments[0].click()", element)

    @testit.step('Delete text in element {element}')
    def delete_text_by_js(self, element):
        self._driver.execute_script("arguments[0].removeAttribute('value')", element)

    @testit.step('Check loader hermes')
    def check_loader(self):
        WebDriverWait(self._driver, 150).until(
            EC.presence_of_element_located(locator=self._LOADER),
            message=f"Не дождался загрузки обновления страницы")
        time.sleep(2)

        return WebDriverWait(self._driver, 150).until(
            EC.presence_of_element_located(locator=self._LOADER),
            message=f"Не дождался загрузки обновления страницы")

    @testit.step('Open tab browser by path class')
    def open(self):
        self._driver.get(f'{self.current_url()}{self.path}')

    @testit.step('Open tab browser by path {path}')
    def open_for_path(self, path):
        self._driver.get(f'{self.base_url()}{self.path}{path}')

    @testit.step('Get base URL')
    def base_url(self) -> str:
        return self._driver.base_url

    @testit.step('Get current URL')
    def current_url(self) -> str:
        return self._driver.current_url

    @testit.step('Close all not current tabs in hermes')
    def close_not_current_tab(self):
        self.check_loader()
        tabs = self.find_elements(locator=self._NOT_CURRENT_TAB)
        for tab in tabs:
            tab.click()

    @testit.step('Move to element {locator}')
    def move_to_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    @testit.step('Find element by {locator}')
    def find_element(self, locator: [str, str], second: int = 40) -> 'WebElement':
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self._driver, timeout=second, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located(locator=locator),
            message=f"Не смог найти элемент по CSS {locator[0]} {locator[1]}")

    @testit.step('Find elements by {locator}')
    def find_elements(self, locator: [str, str], second: int = 40) -> 'list[WebElement]':
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self._driver, timeout=second, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located(locator=locator),
            message=f"Не смог найти элементы по CSS {locator}")

    @testit.step('Select option by value {value} in {locator} ')
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
