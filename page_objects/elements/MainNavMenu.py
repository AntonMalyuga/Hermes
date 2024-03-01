from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class MainNavMenu(BasePage):
    _LOCATOR_A_FULL_NAME = (By.CSS_SELECTOR, '.navbar-default .nav.navbar-nav.navbar-right a')
    _LOCATOR_A_FEEDBACK = (By.CSS_SELECTOR, '.navbar-default [link="/feedback"]')
    _LOCATOR_A_CALENDAR_SLA = (By.CSS_SELECTOR, '.navbar-default a[link="/show_case"]')
    _LOCATOR_A_RELEASE_HISTORY = (By.CSS_SELECTOR, '.navbar-default a[link="/release_notes_history"]')
    _LOCATOR_A_FAQ = (By.CSS_SELECTOR, '.navbar-default a[title="FAQ"]')
    _LOCATOR_A_ALERT_HISTORY = (By.CSS_SELECTOR, '.navbar-default a#notifications_alerts_i')
    _LOCATOR_A_NOTIFICATION = (By.CSS_SELECTOR, '.navbar-default a[title="Срочные уведомления"]')
    _LOCATOR_INPUT_SEARCH_ORDER_ID = (By.CSS_SELECTOR, '#search-task-form #search_by_order_id')
    _LOCATOR_BUTTON_SEARCH_ORDER_ID = (By.CSS_SELECTOR, '#search-task-form button')

    @allure.step("Ввести номер заявки {order_id} в поиск заявки")
    def enter_order_id_in_search_order(self, order_id):
        self.find_element(self._LOCATOR_INPUT_SEARCH_ORDER_ID).send_keys(order_id)

    @allure.step("Получить текст из введённого номера заявки")
    def get_max_length_order_id_in_search_order(self):
        return self.find_element(self._LOCATOR_INPUT_SEARCH_ORDER_ID).get_property('maxLength')

    @allure.step("Кликнуть на поиск заявки")
    def click_search_order(self):
        self.find_element(self._LOCATOR_BUTTON_SEARCH_ORDER_ID).click()

    @allure.step("Получаю имя текущего пользователя")
    def get_user_name(self):
        return self.find_element(self._LOCATOR_A_FULL_NAME).text

    @allure.step("Кликаю на имя текущего пользователя")
    def click_user_name(self):
        self.find_element(self._LOCATOR_A_FULL_NAME).click()

    @allure.step("Кликаю на обратную связь")
    def click_feedback(self):
        self.find_presence_element_with_wait(4, self._LOCATOR_A_FEEDBACK).click()

    @allure.step("Кликаю на календарь SLA")
    def click_calendar_sla(self):
        self.find_element(self._LOCATOR_A_CALENDAR_SLA).click()

    @allure.step("Кликаю на список изменений")
    def click_release_history(self):
        self.find_element(self._LOCATOR_A_RELEASE_HISTORY).click()

    @allure.step("Кликаю на FAQ")
    def click_faq(self):
        self.find_element(self._LOCATOR_A_FAQ).click()

    @allure.step("Кликаю на оповещения")
    def click_notification(self):
        self.find_element(self._LOCATOR_A_NOTIFICATION).click()
