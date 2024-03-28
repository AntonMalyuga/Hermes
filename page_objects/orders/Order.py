from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class Order(BasePage):
    _CHECK_OPEN_ORDER = (By.CSS_SELECTOR, '.tab-content title')
    _LOCATOR_ORDER_ID = (By.XPATH, '//div[text()="Номер заявки:"]/following::div[1]')
    _LOCATOR_ODER_CURRENT_STAGE = (
        By.CSS_SELECTOR, '.panel.panel-small-margin div.panel-body .agg-value:nth-child(3) .agg-key-value__value')
    _LOCATOR_FORM_ODER_CLOSE_STAGE_PASS = (
        By.XPATH, '//select[@name="passDescriptionId"]/optgroup[@label="Ручные переходы"]/option')
    _LOCATOR_FORM_ODER_CLOSE_STAGE_REASON = (By.CSS_SELECTOR, 'select.js--show-reason-description')
    _LOCATOR_FORM_ODER_CLOSE_STAGE_COMMENT = (By.CSS_SELECTOR, '.agg-change-stage-form textarea[name="comment"]')
    _LOCATOR_FORM_BUTTON_CLOSE_STAGE = (By.CSS_SELECTOR, 'div[id^="moveOrderSelector"]')

    def open_order(self, order_id: int):
        time.sleep(7)
        self._driver.get(f'{self._driver.base_url}/aggregator/{order_id}')

    def get_order_id(self) -> int:
        return int(self.find_element(locator=self._LOCATOR_ORDER_ID).text)

    def check_open_order_interface(self) -> bool:
        self.check_loader()
        self.find_element(locator=self._CHECK_OPEN_ORDER).get_property(
            'innerText')

    def check_order_id(self, order_id: int) -> bool:
        self.check_open_order_interface()
        text = self.find_element(locator=self._CHECK_OPEN_ORDER).get_property(
            'innerText')

        if text.find(str(order_id)) != -1:
            return True

    def check_current_stage(self, stage_name: str):
        self.check_open_order_interface()
        text = self.find_element(locator=self._LOCATOR_ODER_CURRENT_STAGE).get_property(
            'innerText')

        if text.find(str(stage_name)) == -1:
            raise Exception(f'Некорректный этап, ожидание {stage_name}, получен {text}')

    def close_stage(self, pass_name: str, next_stage: str, reason: str = '', comment: str = '',
                    is_auto: bool = False, ):
        """Закрытие этапа БП

        Обязательные параметры:
        pass_name - имя перехода
        next_stage - имя следующего этапа

        Необязательные параметры:
        reason- причина
        comment - комментарий
        is_auto - закрытие этапа без проверок
        """
        self.check_open_order_interface()
        try:
            pass_locator = (By.XPATH, f'{self._LOCATOR_FORM_ODER_CLOSE_STAGE_PASS[1]}[text()="{pass_name}"]')
            self.find_element(locator=pass_locator).click()
        except ValueError:
            raise f'Не найден переход {pass_name}'

        if reason:
            time.sleep(3)
            self.selected_element_by_value(value=reason, locator=self._LOCATOR_FORM_ODER_CLOSE_STAGE_REASON)

        if comment:
            time.sleep(3)
            self.find_element(locator=self._LOCATOR_FORM_ODER_CLOSE_STAGE_COMMENT).send_keys(comment)

        time.sleep(3)

        if is_auto:
            self.find_elements(locator=(By.CSS_SELECTOR, f'{self._LOCATOR_FORM_BUTTON_CLOSE_STAGE[1]} button'))[
                1].click()
        else:
            element = self.find_element(locator=(By.CSS_SELECTOR, f'{self._LOCATOR_FORM_BUTTON_CLOSE_STAGE[1]} button'))
            element.click()

        self.check_current_stage(next_stage)
