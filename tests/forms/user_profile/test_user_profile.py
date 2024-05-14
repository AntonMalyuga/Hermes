import time
from page_objects.forms.FormUserProfile import FormUserProfile
from page_objects.elements.Alert import Alert


def test_check_mail_user(driver):
    FormUserProfile(driver).open()
    assert FormUserProfile(driver).get_email() == 'testgermes@yandex.ru12'


def test_check_login(driver):
    FormUserProfile(driver).open()
    assert FormUserProfile(driver).get_login() == FormUserProfile.LOGIN


def test_enter_change_password_on_current_pass(driver):
    FormUserProfile(driver).open()
    time.sleep(2)
    FormUserProfile(driver).enter_current_pass(FormUserProfile.PASSWORD)
    FormUserProfile(driver).enter_new_pass(FormUserProfile.PASSWORD)
    FormUserProfile(driver).enter_confirm_new_pass(FormUserProfile.PASSWORD)
    FormUserProfile(driver).click_save_pass_changes()
    assert Alert(
        driver).get_alert_text() == 'Новый пароль не должен совпадать с уже использованными паролями за последний год'


def test_moscow_number(driver):
    FormUserProfile(driver).open()

    def check_region_moscow_phone_number(telephone_number):

        telephone_number = str(telephone_number)
        if telephone_number[0] == '8':
            return True
        if telephone_number[0] == '+' and telephone_number[1] == '7':
            return True
        else:
            return False

    assert check_region_moscow_phone_number(FormUserProfile(driver).get_phone_number())

