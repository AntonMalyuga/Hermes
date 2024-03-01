import allure
import pytest

from page_objects.elements.UserLoginForm import UserLoginForm
from page_objects.elements.Alert import Alert
from page_objects.elements.MainNavMenu import MainNavMenu
from page_objects.orders.Order import Order


@allure.feature('Главное навигационное меню')
@allure.title('Проверка корректности имени авторизованного пользователя')
@pytest.mark.skip('Необходимо проверить позже')
def test_correct_user_name_on_page(driver):
    UserLoginForm(driver).autorization_default()
    assert MainNavMenu(driver).get_user_name() == 'Малюга Антон Сергеевич'


@pytest.mark.smoke
@allure.feature('Поиск по номеру заявки')
@allure.title('Проверка корректного поиска номера заявки')
@pytest.mark.parametrize('order_id', [1582684, 1582686], ids=['Номер клиентской заявки', 'Номер строительной заявки'])
def test_search_order_id_positive(driver, order_id):
    UserLoginForm(driver).autorization_default()
    MainNavMenu(driver).enter_order_id_in_search_order(order_id)
    MainNavMenu(driver).click_search_order()
    assert Order(driver).check_order_id(order_id)


@allure.feature('Поиск по номеру заявки')
@allure.title('Проверка ошибки при поиске несуществующей заявки')
@pytest.mark.smoke
@pytest.mark.parametrize('order_id', [12], ids=['Номер несуществующей заявки'])
def test_search_order_id_for_important_order(driver, order_id):
    UserLoginForm(driver).autorization_default()
    MainNavMenu(driver).enter_order_id_in_search_order(order_id)
    MainNavMenu(driver).click_search_order()
    assert Alert(driver).get_alert_text() == f'Заявка {order_id} не найдена.'


@allure.feature('Поиск по номеру заявки')
@allure.title('Проверка при поиске незаполненного номера заявки')
@pytest.mark.smoke
def test_search_order_id_for_null_symbol(driver):
    UserLoginForm(driver).autorization_default()
    MainNavMenu(driver).click_search_order()
    text = Alert(driver).get_alert_resource_not_found()
    assert text.find('Не найден маршрут для адреса https://hermes-test.rt.ru/aggregator/') != -1


@allure.feature('Поиск по номеру заявки')
@allure.title('Проверка максимального количества символов для поиска заявки')
@pytest.mark.smoke
def test_max_length_symbol_search_order_id(driver):
    UserLoginForm(driver).autorization_default()
    assert MainNavMenu(driver).get_max_length_order_id_in_search_order() == 15

