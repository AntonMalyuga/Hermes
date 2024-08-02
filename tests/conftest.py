import pytest
from page_objects.elements.UserLoginForm import UserLoginForm


@pytest.fixture(scope='session', autouse=True)
def authorization(driver):
    UserLoginForm.open_by_default()
    if driver.url == 'https://hermes-prod.rt.ru':
        UserLoginForm.authorization_default_2fa()
    else:
        UserLoginForm.authorization_default()
