from page_objects.components.ComponentConnectionParameters import ComponentConnectionParameters
import pytest


@pytest.mark.smoke
def test_component_connection_parameters(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentConnectionParameters(driver).change_connection_parameters(value='Оптика', coordination='Какое-то',
                                                                       conditions='Невероятные', crossing='Оптика',
                                                                       last_mile='Кроссировка', network='Сеть РТ')
