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


def test_close_stage(driver):
    UserLoginForm(driver).autorization_default()
    MainNavMenu(driver).enter_order_id_in_search_order(1596129)
    MainNavMenu(driver).click_search_order()
    Order(driver).close_stage(pass_name='Положительно', is_auto=True)
    Order(driver).close_stage(pass_name='Требуются уточнения у инициатора', is_auto=True)
    Order(driver).close_stage(pass_name='Положительно', is_auto=True)
    Order(driver).close_stage(pass_name='Требуются уточнения у инициатора', is_auto=True)


def test_login(driver):
    UserLoginForm(driver).enter_login_default()
    time.sleep(10)


def test_change_work(driver):
    works = {
        'Восстановление поврежденного канала кабельной канализации': {
            'type': 'СМР',
            'qty': 12,
            'natural_indicator': 'Точки доступа'
        },
        'Восстановление газонного покрытия': {
            'type': 'СМР',
            'qty': 10,
            'natural_indicator': 'Точки доступа'
        }
    }

    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/b2c/works_volumes/1595615/1595616?activeInfrastructureTab=2')
    B2cFormWorkVolume(driver).set_construct_method('Хоз.способ')
    B2cFormWorkVolume(driver).add_works(works)
    B2cFormWorkVolume(driver).close()
    time.sleep(20)


def test_change_specification(driver):
    specifications = {
        'Wi-Fi оборудование 1': {
            'natural_indicator': 'Точки доступа'
        }
    }

    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/b2c/specification/1595778?activeInfrastructureTab=2')
    B2cFormSpecification(driver).set_construct_method('Хоз. способ')
    B2cFormSpecification(driver).add_specification(specifications)
    B2cFormSpecification(driver).close()
    time.sleep(20)


def test_change_control_dates(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1595877')
    ComponentControlDate(driver).change_all_control_dates(10)
    time.sleep(20)


def test_change_other_capital_costs(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1595877')
    ComponentCapitalCosts(driver).add_cost('привет мир', 300)
    time.sleep(10)


def test_change_other_opex_costs(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1595877')
    ComponentOpexCosts(driver).add_cost('привет мир', 300)
    time.sleep(10)


def test_add_file(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1595877')
    ComponentFiles(driver).add_file(name='супер', type='Ведомость ВО (pdf)', file_name='file.txt')
    time.sleep(10)


def test_check_list_wifi(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1597383')
    ComponentCheckListWiFi(driver).add_cost_wifi(value='opex')
    time.sleep(5)


def test_check_list_video(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1597383')
    ComponentCheckListVideo(driver).add_cost_video(value='capex')
    time.sleep(5)


def test_change_material_part(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1597383')
    ComponentPanelMaterialPart(driver).add_material_part(value='1597384', name='Кампуктеры', cost=12345,
                                                         text='Строительный проект B2C #1597383')
    time.sleep(5)


def test_check_additional_income(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1595877')
    ComponentAdditionalIncome(driver).add_addictional_income(name='Вайфай', infrastructure_type='Wi-Fi',
                                                             income_type='WiFi', abonent_type='Приростная', value=10000)
    time.sleep(5)


def test_check_type_project(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1596646')
    ComponentTypeProject(driver).change_type_project(value='ЛИП')
    time.sleep(5)


def test_check_link_sip(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1596646')
<<<<<<< HEAD
    ComponentLinkSip(driver).check_link_sip(lip="https://siptest.rt.ru/", kip="", kip_key="")
    time.sleep(5)


def test_open_hoz(driver):
    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/aggregator/1597719/344')
    Hoz(driver).open_order(ComponentOrdersHierarchy(driver).get_hoz_number())
    time.sleep(5)
=======
    ComponentLinkSip(driver).add_link_sip(lip="https://siptest.rt.ru/", kip="", kip_key="")
    time.sleep(5)
>>>>>>> 97fcc05dc6415d4281afb38d152c94238949cb88
