from page_objects.components.ComponentRFPoint import ComponentRFPoint
import pytest


@pytest.mark.smoke
def test_component_connection_parameters(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1602663')
    ComponentRFPoint(driver).change_rf_point(interface='CUSTOM', equipment='Кампуктеры')