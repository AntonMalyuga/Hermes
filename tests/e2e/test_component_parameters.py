from page_objects.components.ComponentConnectionParameters import ComponentConnectionParameters
from page_objects.elements.UserLoginForm import UserLoginForm


def test_component_connection_parameters(driver):
    UserLoginForm(driver).authorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentConnectionParameters(driver).change_connection_parameters(value='Оптика', coordination='Какое-то',
                                                                       conditions='Невероятные', crossing='Оптика',
                                                                       last_mile='Кроссировка', network='Сеть РТ')
