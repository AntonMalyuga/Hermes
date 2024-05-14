import pytest
import testit

from page_objects.forms.FormB2BWorkVolume import FormB2BWorkVolume


def test_form_b2b_work(driver):
    driver.get('https://hermes-test.rt.ru/aggregator/volumes/1604035')
    FormB2BWorkVolume(driver).fill_and_save_random_works()
