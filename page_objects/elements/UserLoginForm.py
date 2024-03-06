import os
from ..BasePage import BasePage
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


class UserLoginForm(BasePage):
    LOGIN = os.getenv('HERMES_LOGIN')
    PASSWORD = os.getenv('HERMES_PASSWORD')

    _LOCATOR_INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    _LOCATOR_INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    _LOCATOR_BUTTON_SUBMIT_FORM = (By.CSS_SELECTOR, 'form button[type="submit"]')
    _LOCATOR_TEXT_ALERT_ELEMENT = (By.CSS_SELECTOR, 'form .error-container')

    def autorization_with(self, username: str, password: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(username)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    def autorization_default(self):
        self.autorization_with(username=self.LOGIN, password=self.PASSWORD)

    def get_text_alert_error(self) -> str:
        return self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text

    def enter_login(self, login: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    def enter_login_default(self):
        x = self.LOGIN
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(self.LOGIN)

    def enter_password(self, password: str):
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    def click_log_in(self):
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
