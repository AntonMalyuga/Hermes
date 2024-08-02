from page_objects.components.ComponentBindingOT import ComponentBindingOT
import pytest


@pytest.mark.skip('playwrite')
def test_component_connection_parameters(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1604329')
    ComponentBindingOT().change_binding_ot(
        value='АТС-VLG.ARGUS.1371454309, Область Саратовская, Город Саратов, проезд Соколовогорский 1-й, д. 13А')
