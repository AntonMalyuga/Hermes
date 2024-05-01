import time

import pytest
import testit

from page_objects.components.ComponentCreatePreTEOAndTEOOnMap import ComponentCreatePreTEOAndTEOOnMap
from page_objects.forms.B2BMapCreatePreTEOAndTEOOnMap import B2BMapCreatePreTEOAndTEOOnMap
from page_objects.elements.UserLoginForm import UserLoginForm


def test_open_map(driver):
    UserLoginForm(driver).authorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1601552')
    ComponentCreatePreTEOAndTEOOnMap(driver).open_form()
    time.sleep(5000)


def test_click_coordinates(driver):
    UserLoginForm(driver).authorization_default()
    driver.get('https://hermes-test.rt.ru/common/yandex-map/12/1602633')
    B2BMapCreatePreTEOAndTEOOnMap(driver).create_pre_teo_and_teo()
    time.sleep(10)
