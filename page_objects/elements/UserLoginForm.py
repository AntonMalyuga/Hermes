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

    @allure.step("Авторизовываюсь под пользователем {username} с паролем {password}")
    def autorization_with(self, username: str, password: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(username)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    @allure.step("Авторизовываюсь под базовым пользователем")
    def autorization_default(self):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(LOGIN)
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(PASSWORD)
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()

    @allure.step("Получаю ошибку формы")
    def get_text_alert_error(self) -> str:
        return self.find_element(self._LOCATOR_TEXT_ALERT_ELEMENT).text

    @allure.step("Ввожу логин {login}")
    def enter_login(self, login: str):
        self.find_element(self._LOCATOR_INPUT_LOGIN).send_keys(login)

    @allure.step("Ввожу пароль {password}")
    def enter_password(self, password: str):
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    @allure.step("Кликаю на авторизацию")
    def click_log_in(self):
        self.find_element(self._LOCATOR_BUTTON_SUBMIT_FORM).click()
