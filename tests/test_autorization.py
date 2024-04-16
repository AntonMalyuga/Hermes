import pytest
import testit

from page_objects.elements.UserLoginForm import UserLoginForm


@testit.title('Авторизация')
@testit.displayName('Авторизация с валидными данными')
@testit.description('Проверяется авторизация под рабочей учётной записи')
def test_user_authorization_success(driver, base_url):
    UserLoginForm(driver).authorization_default()
    with testit.step('Base URL is current URL' 'Authorization success'):
        assert UserLoginForm(driver).current_url() == base_url


@testit.title('Авторизация')
@testit.displayName('Авторизация с невалидными данными')
@testit.description('Проверяется отображение ошибки при некорретных учётных данных и невозможность попасть в систему под ними')
@pytest.mark.parametrize('login, password',
                         [('MalyugaAS', 'TestPass'), ('TestUser', 'TestPass')],
                         ids=['correct_login_and_not_correct_pass', 'not_correct_login_and_not_correct_pass'])
def test_user_authorization_failed(driver, login, password):
    UserLoginForm(driver).authorization_with(username=login, password=password)
    with testit.step(f'Check text error "Неверные учётные данные"', 'Authorization not successful'):
        assert UserLoginForm(driver).get_text_alert_error() == 'Неверные учётные данные'
