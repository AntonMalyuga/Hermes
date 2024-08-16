from page import Page
from locator import Locator, Select, Input
import testit


class MainNavMenu(Page):
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


    @classmethod
    def enter_order_id_in_search_order(cls, order_id):
        with testit.step(f'Ввести заказ в главном меню "{order_id}"'):
            Input(cls._LOCATOR_INPUT_SEARCH_ORDER_ID).input(order_id)

    @classmethod
    def get_max_length_order_id_in_search_order(cls):
        max_len_search = len(Locator(cls._LOCATOR_INPUT_SEARCH_ORDER_ID).text)
        with testit.step(f'Получить максимальную длину order id в поисковой форме заказа "{max_len_search}"'):
            return max_len_search

    @classmethod
    def click_search_order(cls):
        with testit.step('Нажать кнопку поиска заказа', 'Заказ найден'):
            Locator(cls._LOCATOR_BUTTON_SEARCH_ORDER_ID).click()

    @classmethod
    def get_user_name(cls) -> str:
        user_name = Locator(cls._LOCATOR_A_FULL_NAME).text
        with testit.step(f'Получить имя пользователя из главного меню {user_name}'):
            return user_name

    @classmethod
    def click_user_name(cls):
        with testit.step('Нажать на имя пользователя в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_FULL_NAME).click()

    @classmethod
    def click_feedback(cls):
        with testit.step('Нажать на фидбек в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_FEEDBACK).click()

    @classmethod
    def click_calendar_sla(cls):
        with testit.step('Нажать на календарь СЛА в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_CALENDAR_SLA).click()

    @classmethod
    def click_release_history(cls):
        with testit.step('Нажать на историю релизов в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_RELEASE_HISTORY).click()

    @classmethod
    def click_faq(cls):
        with testit.step('Нажать на FAQ в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_FAQ).click()

    @classmethod
    def click_notification(cls):
        with testit.step('Нажать на уведомления в главном меню', 'Кнопка нажата'):
            Locator(cls._LOCATOR_A_NOTIFICATION).click()
