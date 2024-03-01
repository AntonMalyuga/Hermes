import allure
import pytest

from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Авторизация')
@allure.title("Проверка успешной авторизации пользователя")
@pytest.mark.smoke
def test_user_autorization_success(driver, base_url):
    """Положительная авторизация пользователя в Гермес"""
    UserLoginForm(driver).autorization_default()
    assert UserLoginForm(driver).current_url() == base_url


@allure.feature('Авторизация')
@allure.title("Проверка некорректной авторизации пользователя")
@pytest.mark.smoke
@pytest.mark.parametrize('login, password',
                         [('MalyugaAS', 'TestPass'), ('TestUser', 'TestPass')],
                         ids=['correct_login_and_not_correct_pass', 'not_correct_login_and_not_correct_pass'])
def test_user_autorization_failed(driver, login, password):
    """Отрицательная авторизация пользователя в "Гермес" с некорректным вводом логина и пароля"""
    UserLoginForm(driver).enter_login(login)
    UserLoginForm(driver).enter_password(password)
    UserLoginForm(driver).click_log_in()
    assert UserLoginForm(driver).get_text_alert_error() == 'Неверные учётные данные'