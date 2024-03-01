from ..BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class Alert(BasePage):
    _ALERT = (By.CSS_SELECTOR, '#toast-container span')
    _ALERT_404_STATUS = (By.CSS_SELECTOR, '#toast-container .toast-message')

    @allure.step('Получаю текст бизнес-ошибки в уведомлении')
    def get_alert_text(self) -> str:
        return self.find_presence_element_with_wait(second=2, css_selector=self._ALERT).text

    @allure.step('Получаю тест о 404 ошибке в уведомлении')
    def get_alert_resource_not_found(self):
        return self.find_presence_element_with_wait(second=1, css_selector=self._ALERT_404_STATUS).text
