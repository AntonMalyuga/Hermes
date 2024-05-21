import pytest
from page_objects.elements.UserLoginForm import UserLoginForm


@pytest.fixture(scope='session', autouse=True)
def authorization():
    UserLoginForm.open_by_default()
    UserLoginForm.authorization_default()
