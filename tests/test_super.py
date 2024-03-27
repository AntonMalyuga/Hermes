import time

from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order
from page_objects.orders.b2c.Hoz import Hoz
from page_objects.orders.b2c.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.orders.b2c.b2cFormSpecification import B2cFormSpecification
from page_objects.orders.b2c.ComponentControlDate import ComponentControlDate
from page_objects.orders.b2c.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.orders.b2c.ComponentOpexCosts import ComponentOpexCosts
from page_objects.orders.b2c.ComponentFiles import ComponentFiles
from page_objects.orders.b2c.ComponentCheckListWiFi import ComponentCheckListWiFi
from page_objects.orders.b2c.ComponentCheckListVideo import ComponentCheckListVideo
from page_objects.orders.b2c.ComponentPanelMaterialPart import ComponentPanelMaterialPart
from page_objects.orders.b2c.ComponentAddictionalIncome import ComponentAdditionalIncome
from page_objects.orders.b2c.ComponenOrderstHierarchy import ComponentOrdersHierarchy
from page_objects.orders.b2c.ComponentTypeProject import ComponentTypeProject
from page_objects.orders.b2c.ComponentLinksSip import ComponentLinkSip
from page_objects.b2cCreationSMROrder import B2CCreateSMROrder


def test_creation_smr(driver):
    smr = {
        'building_type': 'Комплексная новостройка',
        'floors': 9,
        'entrances': 4,
        'flats': 4,
        'dh_counter': 100,
        'commerce_plan': 10,
        'ap_year': '2019',
        'location_name': 'Москва',
        'client': '111111111',
        'obj_type': 'Многоквартирный дом'
    }

    UserLoginForm(driver).autorization_default()
    B2CCreateSMROrder(driver).open()
    B2CCreateSMROrder(driver).create_smr_order_form(smr)
    B2CCreateSMROrder(driver).set_random_street_and_house()
    time.sleep(5)
