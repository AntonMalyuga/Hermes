import time

from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order
from page_objects.orders.b2c.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.orders.b2c.b2cFormSpecification import B2cFormSpecification
from page_objects.orders.b2c.ComponentControlDate import ComponentControlDate
from page_objects.orders.b2c.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.orders.b2c.ComponentOpexCosts import ComponentOpexCosts
from page_objects.orders.b2c.ComponentFiles import ComponentFiles
from page_objects.orders.b2c.ComponentCheckListWiFi import ComponentCheckListWiFi


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
    time.sleep(10)