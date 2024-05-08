from page_objects.components.ComponentRFPoint import ComponentRFPoint
from page_objects.elements.UserLoginForm import UserLoginForm


def test_component_connection_parameters(driver):
    UserLoginForm(driver).authorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentRFPoint(driver).change_rf_point(interface='CUSTOM', equipment='Кампуктеры')