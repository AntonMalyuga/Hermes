import os
from dotenv import load_dotenv
from locator import Locator, Input
from page import Page
import testit

load_dotenv()


class UserLoginForm(Page):
    name = 'Форма авторизации'
    path = ''

    LOGIN = os.getenv('HERMES_LOGIN')
    PASSWORD = os.getenv('HERMES_PASSWORD')

    _INPUT_LOGIN = '//input[@id="username"]'
    _INPUT_PASSWORD = '//input[@id="password"]'
    _BUTTON_SUBMIT_FORM = '//button[@type="submit"]'
    _TEXT_ALERT_ELEMENT = '//form//div[@class="error-container"]'
    _INPUT_CONFIRM_ACCOUNT = '//input[@name="confirmation_code"]'

    @staticmethod
    def authorization_default():
        with testit.step('Базовая авторизация', 'Успешная авторизация'):
            UserLoginForm.authorization_with(username=UserLoginForm.LOGIN, password=UserLoginForm.PASSWORD)

    @staticmethod
    def authorization_with(username: str, password: str):
        with testit.step('Авторизация с логином и паролем', 'Успешная авторизация'):
            UserLoginForm.enter_login(username)
            UserLoginForm.enter_password(password)
            UserLoginForm.click_log_in()

    @staticmethod
    def authorization_default_2fa():
        with testit.step('Авторизация с логином и паролем по 2FA', 'Успешная авторизация'):
            UserLoginForm.authorization_with(username=UserLoginForm.LOGIN, password=UserLoginForm.PASSWORD)
            UserLoginForm.enter_2fa_password()
            UserLoginForm.click_log_in()

    @staticmethod
    def get_text_alert_error() -> str:
        text_alert = Locator(UserLoginForm._TEXT_ALERT_ELEMENT).text
        with testit.step(f'Получить текст ошибки "{text_alert}"', 'Текст ошибки получен'):
            return text_alert

    @staticmethod
    def enter_2fa_password():
        password_2fa = input('Ввести код из почты для 2FA авторизации:')
        with testit.step(f'Ввести второй код 2FA из почты', 'Код введён'):
            Input(UserLoginForm._INPUT_CONFIRM_ACCOUNT).input(password_2fa)

    @staticmethod
    def enter_login(login: str):
        with testit.step(f'Ввести логин "{login}"', 'Логин введен'):
            Input(UserLoginForm._INPUT_LOGIN).input(login)

    @staticmethod
    def enter_password(password: str):
        with testit.step(f'Ввести пароль "{password}"', 'Пароль введен'):
            Input(UserLoginForm._INPUT_PASSWORD).input(password)

    @staticmethod
    def click_log_in():
        with testit.step('Нажать кнопку "войти"', 'Успешный вход в аккаунт'):
            Locator(UserLoginForm._BUTTON_SUBMIT_FORM).click()
