import time
import allure
from page_objects.UserProfile import UserProfile
from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.Alert import Alert
from page_objects.elements.UserLoginForm import PASSWORD, LOGIN


@allure.feature('Профиль пользователя')
@allure.title("Проверка значения почты по умолчанию")
def test_check_mail_user(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/user_management/sso/user_profile')
    assert UserProfile(driver).get_email() == 'testgermes@yandex.ru12'


@allure.feature('Профиль пользователя')
@allure.title("Проверка на соответствие логина с логином авторизации")
def test_check_login(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/user_management/sso/user_profile')
    assert UserProfile(driver).get_login() == LOGIN


@allure.feature('Профиль пользователя')
@allure.title("Проверка замены пароля на существующий пароль")
def test_enter_change_password_on_current_pass(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/user_management/sso/user_profile')
    time.sleep(2)
    UserProfile(driver).enter_current_pass(PASSWORD)
    UserProfile(driver).enter_new_pass(PASSWORD)
    UserProfile(driver).enter_confirm_new_pass(PASSWORD)
    UserProfile(driver).click_save_pass_changes()
    assert Alert(
        driver).get_alert_text() == 'Новый пароль не должен совпадать с уже использованными паролями за последний год'


@allure.feature('Профиль пользователя')
@allure.title("Проверка на московский номер")
def test_moscow_number(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/user_management/sso/user_profile')

    def check_region_moskov_phone_number(telepnone_number):

        telepnone_number = str(telepnone_number)
        if telepnone_number[0] == '8':
            return True
        if telepnone_number[0] == '+' and telepnone_number[1] == '7':
            return True
        else:
            return False

    assert check_region_moskov_phone_number(UserProfile(driver).get_phone_number())
