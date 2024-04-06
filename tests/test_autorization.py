import pytest
import testit

from page_objects.elements.UserLoginForm import UserLoginForm


@testit.title('Authorization')
@testit.displayName('Positive authorization')
@testit.description('Authorization positive test')
def test_user_authorization_success(driver, base_url):
    UserLoginForm(driver).authorization_default()
    with testit.step('Base URL is current URL' 'Authorization success'):
        assert UserLoginForm(driver).current_url() == base_url


@testit.title('Authorization')
@testit.displayName('Negative authorization')
@testit.description('Authorization negative test with invalid login and password')
@pytest.mark.parametrize('login, password',
                         [('MalyugaAS', 'TestPass'), ('TestUser', 'TestPass')],
                         ids=['correct_login_and_not_correct_pass', 'not_correct_login_and_not_correct_pass'])
def test_user_authorization_failed(driver, login, password):
    UserLoginForm(driver).authorization_with(username=login, password=password)
    with testit.step(f'Check text error "Неверные учётные данные"', 'Authorization not successful'):
        assert UserLoginForm(driver).get_text_alert_error() == 'Неверные учётные данные'
