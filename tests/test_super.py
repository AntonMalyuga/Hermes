import time

from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order
from page_objects.orders.b2c.Hoz import Hoz
from page_objects.orders.b2c.SMR import SMR
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
from page_objects.orders.b2c.ComponentAddressParameters import ComponentAdressParameters
from page_objects.orders.b2c.ComponentLoaderDH import ComponentLoaderDH
from page_objects.b2cObjectOrder import B2CObjectOrder
from page_objects.orders.b2c.ComponentNumberDSOFU import ComponentNumberDSOFU


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

    # smr = {
    #     'building_type': 'Коттеджный посёлок/частный сектор',
    #     'location_name': 'Калужская область',
    #     'area': 'Боровский район',
    #     'village': 'Рыжково Деревня',
    #     'area_name': 'Тест1',
    #     'commerce_plan': '4',
    #     'ap_year': '2019'
    # }

    UserLoginForm(driver).autorization_default()
    B2CCreateSMROrder(driver).open()
    B2CCreateSMROrder(driver).create_smr_order_form(smr)
    B2CCreateSMROrder(driver).set_random_street_and_house()
    time.sleep(5)


def test_component_adress_parameters(driver):
    UserLoginForm(driver).autorization_default()
    SMR(driver).open_order(1598797)
    ComponentLoaderDH(driver).add_dh(
        link='https://yandex.ru/maps/?um=constructor%3Ad3ebc1e3d9867f5332fa30f4418892459de4b6fc1da211fda23de869fe708924&source=constructorLink',
        file_name='Загрузка_дх.xlsx')
    ComponentAdressParameters(driver).add_abonents(abonents=5)


def test_b2c_object_order(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/b2c/group_orders/1598830')
    B2CObjectOrder(driver).add_contractor(discount=10, contractor='Саратовский', frame=555555)


def test_number_dsofu(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1598830/344')
    ComponentNumberDSOFU(driver).add_DSOFU(kode=1223455667)
