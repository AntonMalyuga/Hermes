import time

import pytest
from page_objects.elements.UserLoginForm import UserLoginForm


@pytest.fixture(autouse=True)
def authorization(driver):
    UserLoginForm(driver).authorization_default_2fa()
