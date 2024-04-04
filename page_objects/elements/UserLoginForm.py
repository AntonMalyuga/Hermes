import os
from ..BasePage import BasePage
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import testit

load_dotenv()


class UserLoginForm(BasePage):
    LOGIN = os.getenv('HERMES_LOGIN')
    PASSWORD = os.getenv('HERMES_PASSWORD')

    _LOCATOR_INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    _LOCATOR_INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    _LOCATOR_BUTTON_SUBMIT_FORM = (By.CSS_SELECTOR, 'form button[type="submit"]')
    _LOCATOR_TEXT_ALERT_ELEMENT = (By.CSS_SELECTOR, 'form .error-container')

    @testit.step('Authorization with {login} and {password}')
    def authorization_with(self, username: str, password: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(username)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    @testit.step('Authorization default')
    def authorization_default(self):
        self.authorization_with(username=self.LOGIN, password=self.PASSWORD)

    @testit.step('Get alert text')
    def get_text_alert_error(self) -> str:
        return self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text

    @testit.step('Enter login {login}')
    def enter_login(self, login: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    @testit.step('Enter login by default')
    def enter_login_default(self):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(self.LOGIN)

    @testit.step('Enter password {password}')
    def enter_password(self, password: str):
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    @testit.step('Click log in button')
    def click_log_in(self):
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
