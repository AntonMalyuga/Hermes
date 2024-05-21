from locator import Locator
from selenium.webdriver.common.by import By
import testit


class MainNavMenu:
    name = 'Навигационное меню'

    _LOCATOR_A_FULL_NAME = '.navbar-default .nav.navbar-nav.navbar-right a'
    _LOCATOR_A_FEEDBACK = '.navbar-default [link="/feedback"]'
    _LOCATOR_A_CALENDAR_SLA = '.navbar-default a[link="/show_case"]'
    _LOCATOR_A_RELEASE_HISTORY = '.navbar-default a[link="/release_notes_history"]'
    _LOCATOR_A_FAQ = '.navbar-default a[title="FAQ"]'
    _LOCATOR_A_ALERT_HISTORY = '.navbar-default a#notifications_alerts_i'
    _LOCATOR_A_NOTIFICATION = '.navbar-default a[title="Срочные уведомления"]'
    _LOCATOR_INPUT_SEARCH_ORDER_ID = '#search-task-form #search_by_order_id'
    _LOCATOR_BUTTON_SEARCH_ORDER_ID = '#search-task-form button'


    @staticmethod
    def enter_order_id_in_search_order(order_id):
        with testit.step(f'Ввести заказ в главном меню "{order_id}"'):
            Locator(MainNavMenu._LOCATOR_INPUT_SEARCH_ORDER_ID).input(order_id)

    @staticmethod
    def get_max_length_order_id_in_search_order():
        max_len_search = Locator(MainNavMenu._LOCATOR_INPUT_SEARCH_ORDER_ID).text()
        with testit.step(f'Получить максимальную длину order id в поисковой форме заказа "{max_len_search}"'):
            return max_len_search

    @staticmethod
    def click_search_order():
        with testit.step('Нажать кнопку поиска заказа', 'Заказ найден'):
            Locator(MainNavMenu._LOCATOR_BUTTON_SEARCH_ORDER_ID).click()

    @staticmethod
    def get_user_name() -> str:
        user_name = str(Locator(MainNavMenu._LOCATOR_A_FULL_NAME).text())
        with testit.step('Получить имя пользователя из главного меню {user_name}'):
            return user_name

    @staticmethod
    def click_user_name():
        with testit.step('Нажать на имя пользователя в главном меню', 'Кнопка нажата'):
            Locator(MainNavMenu._LOCATOR_A_FULL_NAME).click()

    @staticmethod
    def click_feedback():
        with testit.step('Нажать на фидбек в главном меню', 'Кнопка нажата'):
            Locator(MainNavMenu._LOCATOR_A_FEEDBACK).click()

    @staticmethod
    def click_calendar_sla():
        with testit.step('Нажать на календарь СЛА в главном меню', 'Кнопка нажата'):
            Locator(MainNavMenu._LOCATOR_A_CALENDAR_SLA).click()

    @staticmethod
    def click_release_history():
        with testit.step('Нажать на историю релизов в главном меню', 'Кнопка нажата'):
            Locator(MainNavMenu._LOCATOR_A_RELEASE_HISTORY).click()

    @staticmethod
    def click_faq(self):
        with testit.step('Нажать на FAQ в главном меню', 'Кнопка нажата'):
            Locator(MainNavMenu._LOCATOR_A_FAQ).click()

    @staticmethod
    def click_notification(self):
        with testit.step('Нажать на уведомления в главном меню', 'Кнопка нажата'):
            Locator(self._LOCATOR_A_NOTIFICATION).click()
