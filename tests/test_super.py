import time

from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order
from page_objects.orders.b2c.Hoz import Hoz
from page_objects.b2cCreationSMROrder import B2CCreateSMROrder


def test_creation_smr(driver):
    UserLoginForm(driver).autorization_default()
    B2CCreateSMROrder(driver).open()
