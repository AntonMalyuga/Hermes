import time
from page_objects.components.ComponentCreatePreTEOAndTEOOnMap import ComponentCreatePreTEOAndTEOOnMap
from page_objects.forms.FormB2BMapCreatePreTEOAndTEOOnMap import FormB2BMapCreatePreTEOAndTEOOnMap
import pytest



@pytest.mark.smoke
def test_open_map(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/1601552')
    ComponentCreatePreTEOAndTEOOnMap(driver).open_form()
    time.sleep(5000)

@pytest.mark.smoke
def test_click_coordinates(driver):
    driver.get('https://hermes-test.rt.ru/common/yandex-map/12/1603826')
    FormB2BMapCreatePreTEOAndTEOOnMap(driver).create_pre_teo_and_teo()
