import testit
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class UserProfile(BasePage):
    _LOCATOR_INPUT_EMAIL = (By.CSS_SELECTOR, '.form-horizontal input.form-control')
    _LOCATOR_INPUT_LOGIN = (By.CSS_SELECTOR, 'input[name="new_login"]')
    _LOCATOR_INPUT_PASSWORD = (
        By.CSS_SELECTOR, '[action="/user_management/sso/user_profile/change_login"] input[name="current_password"]')
    _LOCATOR_BUTTON_CHANGE_PASSWORD = (
        By.CSS_SELECTOR, 'form[action="/user_management/sso/user_profile/change_password"] button')
    _LOCATOR_INPUT_CURRENT_PASSWORD = (
        By.CSS_SELECTOR, '[action="/user_management/sso/user_profile/change_password"] input[name="current_password"]')
    _LOCATOR_INPUT_NEW_PASSWORD = (By.CSS_SELECTOR, 'input[name="new_password"]')
    _LOCATOR_INPUT_SUBMIT_NEW_PASSWORD = (By.CSS_SELECTOR, 'input[name="new_password_repeat"]')
    _LOCATOR_INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[id="param0"]')
    _LOCATOR_BUTTON_SAVE_PHONE = (
        By.CSS_SELECTOR, 'form[action="/user_management/sso/user_profile/change_params"] button')
    _LOCATOR_SELECT_DEFAULT_ROLE = (By.CSS_SELECTOR, 'select[name="default_role"] option[value="344"]')
    _LOCATOR_BUTTON_SAVE_ROLE = (
        By.CSS_SELECTOR,
        'form[action="https://hermes-test.rt.ru/user_management/sso/user_profile/change_settings"] button')

    @testit.step('Get email in user profile')
    def get_email(self):
        return self.find_element(self._LOCATOR_INPUT_EMAIL).get_property('value')

    @testit.step('Get login in user profile')
    def get_login(self):
        return self.find_element(self._LOCATOR_INPUT_LOGIN).get_property('value')

    @testit.step('Enter password in user profile')
    def enter_password(self, password):
        self.find_element(self._LOCATOR_INPUT_PASSWORD).send_keys(password)

    @testit.step('Enter currently password in user profile')
    def enter_current_pass(self, password):
        self.find_element(self._LOCATOR_INPUT_CURRENT_PASSWORD).send_keys(password)

    @testit.step('Enter new password in user profile')
    def enter_new_pass(self, password):
        self.find_element(self._LOCATOR_INPUT_NEW_PASSWORD).send_keys(password)

    @testit.step('Enter confirm new password in user profile')
    def enter_confirm_new_pass(self, password):
        self.find_element(self._LOCATOR_INPUT_SUBMIT_NEW_PASSWORD).send_keys(password)

    @testit.step('Click change password in user profile')
    def click_save_pass_changes(self):
        self.find_element(self._LOCATOR_BUTTON_CHANGE_PASSWORD).click()

    @testit.step('Get telephone number in user profile')
    def get_phone_number(self):
        return self.find_element(self._LOCATOR_INPUT_PHONE_NUMBER).get_property('value')

    @testit.step('Click save telephone number in user profile')
    def click_save_phone(self):
        self.find_element(self._LOCATOR_BUTTON_SAVE_PHONE).click()

    @testit.step('Get default role in user profile')
    def get_default_role(self):
        return self.find_element(self._LOCATOR_SELECT_DEFAULT_ROLE).get_property('innerText')

    @testit.step('Click save change role in user profile')
    def click_save_role(self):
        self.find_element(self._LOCATOR_BUTTON_SAVE_ROLE).click()
