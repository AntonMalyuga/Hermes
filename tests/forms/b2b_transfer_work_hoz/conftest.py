import pytest
from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz


@pytest.fixture
def order_id() -> int:
    return 1602635


@pytest.fixture
def form(driver, order_id):
    FormB2BTransferWorkHoz(driver).open_form(order_id)
