import testit
from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.Alert import Alert
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order


@testit.title('Навигационное меню')
@testit.displayName('Check user name on main menu')
@testit.description('Check user full name on main menu')
def test_correct_user_name_on_page(driver):
    UserLoginForm(driver).authorization_default()
    assert MainNavMenu(driver).get_user_name() == 'Малюга Антон Сергеевич'


@testit.title('Навигационное меню')
@testit.displayName('Check open order')
@testit.description('Check open order after enter in search order')
def test_search_order_id_positive(driver, order_id):
    UserLoginForm(driver).authorization_default()
    MainNavMenu(driver).enter_order_id_in_search_order(order_id)
    MainNavMenu(driver).click_search_order()
    assert Order(driver).check_order_id(order_id)


@testit.title('Навигационное меню')
@testit.displayName('Check alert not valid order')
@testit.description('Check alert not valid order in search order')
def test_search_order_id_for_important_order(driver, order_id):
    UserLoginForm(driver).authorization_default()
    MainNavMenu(driver).enter_order_id_in_search_order(order_id)
    MainNavMenu(driver).click_search_order()
    assert Alert(driver).get_alert_text() == f'Заявка {order_id} не найдена.'


@testit.title('Навигационное меню')
@testit.displayName('Check alert empty order')
@testit.description('Check alert empty order in search order')
def test_search_order_id_for_null_symbol(driver):
    UserLoginForm(driver).authorization_default()
    MainNavMenu(driver).click_search_order()
    text = Alert(driver).get_alert_resource_not_found()
    assert text.find('Не найден маршрут для адреса https://hermes-test.rt.ru/aggregator/') != -1


@testit.title('Навигационное меню')
@testit.displayName('Check max length order symbol')
@testit.description('Check max length order symbol in search order')
def test_max_length_symbol_search_order_id(driver):
    UserLoginForm(driver).authorization_default()
    assert MainNavMenu(driver).get_max_length_order_id_in_search_order() == 15
