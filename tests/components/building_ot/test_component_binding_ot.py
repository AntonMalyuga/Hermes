from page_objects.components.ComponentBindingOT import ComponentBindingOT
from page_objects.elements.UserLoginForm import UserLoginForm
import pytest


@pytest.mark.smoke
def test_component_connection_parameters(driver):
    UserLoginForm(driver).authorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentBindingOT(driver).change_binding_ot(
        value='АТС-VLG.ARGUS.1371454309, Область Саратовская, Город Саратов, проезд Соколовогорский 1-й, д. 13А')
