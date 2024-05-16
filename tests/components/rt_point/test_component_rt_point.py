from page_objects.components.ComponentRTPoint import ComponentRTPoint
import pytest


@pytest.mark.smoke
def test_component_connection_parameters(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentRTPoint(driver).change_rt_point(interface='CUSTOM', equipment='Какое-то')