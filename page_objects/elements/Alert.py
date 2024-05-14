import testit
from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class Alert(BasePage):
    name = 'Предупреждение'

    # _ALERT = (By.CSS_SELECTOR, '#toast-container span')
    # _ALERT_404_STATUS = (By.CSS_SELECTOR, '#toast-container .toast-message')

    # def check_alert(self):
    #     if len(self.find_elements(self._ALERT)) == 0:
    #         return True
    #     else:
    #         raise f'Получена ошибка в приложении: {self.get_alert_text()}'
    #
    # def get_alert_text(self) -> str:
    #     alert_text = str(self.find_presence_element_with_wait(second=2, css_selector=self._ALERT).text)
    #     with testit.step(f'Получить текст предупреждения "{alert_text}"'):
    #         return alert_text

    def get_alert_resource_not_found(self):
        alert_text = str(self.find_presence_element_with_wait(second=1, css_selector=self._ALERT_404_STATUS).text)
        with testit.step(f'Получить предупреждение об ошибке если ресурс не найден "{alert_text}"'):
            return alert_text
