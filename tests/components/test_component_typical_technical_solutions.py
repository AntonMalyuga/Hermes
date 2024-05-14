import time

from page_objects.components.ComponentTypicalTechnicalSolutions import ComponentTypicalTechnicalSolutions
from page_objects.elements.UserLoginForm import UserLoginForm


def test_component_typical_technical_solutions(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1603860')
    ComponentTypicalTechnicalSolutions(driver).set_typical_technical_solutions()
    time.sleep(10)
