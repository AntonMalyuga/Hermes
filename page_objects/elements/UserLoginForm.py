from ..BasePage import BasePage
from selenium.webdriver.common.by import By

import allure

LOGIN = 'Логин'
PASSWORD = 'Пароль'


class UserLoginForm(BasePage):
    _LOCATOR_INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    _LOCATOR_INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    _LOCATOR_BUTTON_SUBMIT_FORM = (By.CSS_SELECTOR, 'form button[type="submit"]')
    _LOCATOR_TEXT_ALERT_ELEMENT = (By.CSS_SELECTOR, 'form .error-container')

    def autorization_with(self, username: str, password: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(username)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    def autorization_default(self):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(LOGIN)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(PASSWORD)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    def get_text_alert_error(self) -> str:
        return self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text

    def enter_login(self, login: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    def enter_password(self, password: str):
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    def click_log_in(self):
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
