from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import testit


class Order(BasePage):
    id = ''
    name = ''

    _CHECK_OPEN_ORDER = (By.CSS_SELECTOR, '.tab-content title')
    _LOCATOR_ORDER_ID = (By.XPATH, '//div[text()="Номер заявки:"]/following::div[1]')

    def open_order(self, order_id: int):
        with testit.step(f'Открыть заявку по схеме "{self.name}": {order_id}'):
            time.sleep(7)
            self._driver.get(f'{self._driver.base_url}/aggregator/{order_id}')

    def get_order_id(self) -> int:
        self.check_loader()
        order_id = int(self.find_element(locator=self._LOCATOR_ORDER_ID).text)
        with testit.step(f'Получить номер заявки: {order_id}'):
            return order_id

    @testit.step(f'Дождаться открытия заявки')
    def check_open_order_interface(self):
        self.check_loader()
        self.find_element(locator=self._CHECK_OPEN_ORDER).get_property(
            'innerText')

    def check_order_id(self, order_id: int) -> bool:
        self.check_open_order_interface()
        text = self.find_element(locator=self._CHECK_OPEN_ORDER).get_property(
            'innerText')

        if text.find(str(order_id)) != -1:
            with testit.step(f'Проверка заявки в форме заявки:{order_id}'):
                return True
