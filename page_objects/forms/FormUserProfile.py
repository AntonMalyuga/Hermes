import testit
from locator import Locator, Input, Select
from page import Page


class FormUserProfile(Page):
    name = 'Профиль пользователя'
    path = 'user_management/sso/user_profile'

    _LOCATOR_INPUT_EMAIL = '.form-horizontal input.form-control'
    _LOCATOR_INPUT_LOGIN = 'input[name="new_login"]'
    _LOCATOR_INPUT_PASSWORD = '[action="/user_management/sso/user_profile/change_login"] input[name="current_password"]'
    _LOCATOR_BUTTON_CHANGE_PASSWORD = 'form[action="/user_management/sso/user_profile/change_password"] button'
    _LOCATOR_INPUT_CURRENT_PASSWORD = '[action="/user_management/sso/user_profile/change_password"] input[name="current_password"]'
    _LOCATOR_INPUT_NEW_PASSWORD = 'input[name="new_password"]'
    _LOCATOR_INPUT_SUBMIT_NEW_PASSWORD = 'input[name="new_password_repeat"]'
    _LOCATOR_INPUT_PHONE_NUMBER = 'input[id="param0"]'
    _LOCATOR_BUTTON_SAVE_PHONE = 'form[action="/user_management/sso/user_profile/change_params"] button'
    _LOCATOR_SELECT_DEFAULT_ROLE = 'select[name="default_role"] option[value="344"]'
    _LOCATOR_BUTTON_SAVE_ROLE = 'form[action="https://hermes-test.rt.ru/user_management/sso/user_profile/change_settings"] button'

    @classmethod
    @testit.step('Get email in user profile')
    def get_email(cls):
        return Input(cls._LOCATOR_INPUT_EMAIL).input('value')

    @classmethod
    @testit.step('Get login in user profile')
    def get_login(cls):
        return Input(cls._LOCATOR_INPUT_LOGIN).input('value')

    @classmethod
    @testit.step('Enter password in user profile')
    def enter_password(cls, password):
        Input(cls._LOCATOR_INPUT_PASSWORD).input(password)

    @classmethod
    @testit.step('Enter currently password in user profile')
    def enter_current_pass(cls, password):
        Input(cls._LOCATOR_INPUT_CURRENT_PASSWORD).input(password)

    @classmethod
    @testit.step('Enter new password in user profile')
    def enter_new_pass(cls, password):
        Input(cls._LOCATOR_INPUT_NEW_PASSWORD).input(password)

    @classmethod
    @testit.step('Enter confirm new password in user profile')
    def enter_confirm_new_pass(cls, password):
        Input(cls._LOCATOR_INPUT_SUBMIT_NEW_PASSWORD).input(password)

    @classmethod
    @testit.step('Click change password in user profile')
    def click_save_pass_changes(cls):
        Locator(cls._LOCATOR_BUTTON_CHANGE_PASSWORD).click()

    @classmethod
    @testit.step('Get telephone number in user profile')
    def get_phone_number(cls):
        return Input(cls._LOCATOR_INPUT_PHONE_NUMBER).text

    @classmethod
    @testit.step('Click save telephone number in user profile')
    def click_save_phone(cls):
        Locator(cls._LOCATOR_BUTTON_SAVE_PHONE).click()

    @classmethod
    @testit.step('Get default role in user profile')
    def get_default_role(cls):
        return Locator(cls._LOCATOR_SELECT_DEFAULT_ROLE).text

    @classmethod
    @testit.step('Click save change role in user profile')
    def click_save_role(cls):
        Locator(cls._LOCATOR_BUTTON_SAVE_ROLE).click()
