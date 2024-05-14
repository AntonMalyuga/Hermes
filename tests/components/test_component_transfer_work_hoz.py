import time

from page_objects.components.ComponentB2BTransferWorkHoz import ComponentB2BTransferWorkHoz


def test_component_transfer_work_hoz(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1603896')
    ComponentB2BTransferWorkHoz(driver).open_form_transfer_hoz_work()
