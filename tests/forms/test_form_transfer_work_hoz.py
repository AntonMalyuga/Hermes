import time

from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz


def test_component_transfer_work_hoz(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/works/1603896')
    FormB2BTransferWorkHoz(driver).set_all_works_hoz()
