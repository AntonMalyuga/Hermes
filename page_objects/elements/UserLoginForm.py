import os
from ..BasePage import BasePage
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import testit

load_dotenv()


class UserLoginForm(BasePage):
    name = 'Форма авторизации'

    LOGIN = os.getenv('HERMES_LOGIN')
    PASSWORD = os.getenv('HERMES_PASSWORD')

    _LOCATOR_INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    _LOCATOR_INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    _LOCATOR_BUTTON_SUBMIT_FORM = (By.CSS_SELECTOR, 'form button[type="submit"]')
    _LOCATOR_TEXT_ALERT_ELEMENT = (By.CSS_SELECTOR, 'form .error-container')
    _LOCATOR_INPUT_CONFIRM_ACCOUT = (By.XPATH, '//input[@name="confirmation_code"]')

    def authorization_default(self):
        with testit.step('Базовая авторизация', 'Успешная авторизация'):
            self.authorization_with(username=self.LOGIN, password=self.PASSWORD)

    def authorization_with(self, username: str, password: str):
        with testit.step('Авторизация с логином и паролем', 'Успешная авторизация'):
            self._enter_login(username)
            self._enter_password(password)
            self._click_log_in()

    def authorization_default_2fa(self):
        with testit.step('Авторизация с логином и паролем по 2FA', 'Успешная авторизация'):
            self.authorization_with(username=self.LOGIN, password=self.PASSWORD)
            self._enter_2fa_password()
            self._click_log_in()

    def get_text_alert_error(self) -> str:
        text_alert = self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text
        with testit.step(f'Получить текст ошибки "{text_alert}"', 'Текст ошибки получен'):
            return text_alert

    def _enter_2fa_password(self):
        password_2fa = input('Ввести код из почты для 2FA авторизации:')
        with testit.step(f'Ввести второй код 2FA из почты', 'Код введён'):
            self.find_element(self._LOCATOR_INPUT_CONFIRM_ACCOUT).send_keys(password_2fa)

    def _enter_login(self, login: str):
        with testit.step(f'Ввести логин "{login}"', 'Логин введен'):
            self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    def _enter_password(self, password: str):
        with testit.step(f'Ввести пароль "{password}"', 'Пароль введен'):
            self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    def _click_log_in(self):
        with testit.step('Нажать кнопку "войти"', 'Успешный вход в аккаунт'):
            self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
