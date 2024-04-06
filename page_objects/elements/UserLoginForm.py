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

    @testit.step('Authorization with login and password')
    def authorization_with(self, username: str, password: str):
        self._enter_login(username)
        self._enter_password(password)
        self._click_log_in()

    @testit.step('Authorization default')
    def authorization_default(self):
        self.authorization_with(username=self.LOGIN, password=self.PASSWORD)

    @testit.step('Get alert text')
    def get_text_alert_error(self) -> str:
        text_alert = self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text
        with testit.step(f'Get alert text {text_alert}', 'Text alert received'):
            return text_alert

    def _enter_login(self, login: str):
        with testit.step(f'Enter the login {login}', 'login was entered'):
            self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    def _enter_password(self, password: str):
        with testit.step(f'Enter the password {password}', 'password was entered'):
            self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    def _click_log_in(self):
        with testit.step('Click log in', 'login was entered'):
            self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
