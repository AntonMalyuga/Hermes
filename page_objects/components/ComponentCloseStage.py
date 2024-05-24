from selenium.webdriver.common.by import By
import time
import testit


class ComponentCloseStage:

    name = 'Управление этапом'

    _CHECK_OPEN_ORDER = '.tab-content title')

    _LOCATOR_FORM_ODER_CLOSE_STAGE_PASS = (
        By.XPATH, '//select[@name="passDescriptionId"]/optgroup[@label="Ручные переходы"]/option')
    _LOCATOR_FORM_ODER_CLOSE_STAGE_REASON = 'select.js--show-reason-description')
    _LOCATOR_FORM_ODER_CLOSE_STAGE_COMMENT = '.agg-change-stage-form textarea[name="comment"]')
    _LOCATOR_FORM_BUTTON_CLOSE_STAGE = 'div[id^="moveOrderSelector"]')

    @testit.step(f'Check opening interface order')
    def check_open_order_interface(self):
        with testit.step('Проверить открытие заявки в интерфейсе'):
            self.check_loader()
            self.find_element(locator=self._CHECK_OPEN_ORDER).get_property(
                'innerText')

    def __set_pass(self, pass_name: str):
        with testit.step(f'Выбрать переход: {pass_name}'):
            try:
                pass_locator = f'{self._LOCATOR_FORM_ODER_CLOSE_STAGE_PASS[1]}[text()="{pass_name}"]')
                self.find_element(locator=pass_locator).click()

            except ValueError:
                raise f'Не найден переход {pass_name}'

    def __set_reason(self, reason: str):
        with testit.step(f'Установить причину: "{reason}"'):
            self.selected_element_by_value(value=reason, locator=self._LOCATOR_FORM_ODER_CLOSE_STAGE_REASON)

    def __set_comment(self, comment: str):
        with testit.step(f'Установить комментарий: "{comment}"'):
            self.find_element(locator=self._LOCATOR_FORM_ODER_CLOSE_STAGE_COMMENT).send_keys(comment)

    def __click_go(self):
        with testit.step('Нажать "Перейти"'):
            self.find_element(locator=f'{self._LOCATOR_FORM_BUTTON_CLOSE_STAGE[1]} button')).click()

    def __click_go_auto(self):
        with testit.step('Нажать "Перейти без проверок"'):
            self.find_elements(locator=f'{self._LOCATOR_FORM_BUTTON_CLOSE_STAGE[1]} button'))[
                1].click()

    def close_stage(self, pass_name: str, next_stage: str = '', reason: str = '', comment: str = '',
                    is_auto: bool = False):
        with testit.step(f'Закрыть переход'):

            self.check_loader()
            self.__set_pass(pass_name)
            self.check_loader()

            if reason:
                time.sleep(3)
                self.__set_reason(reason)

            if comment:
                time.sleep(3)
                self.__set_comment(comment)

            time.sleep(3)

            if is_auto:
                self.__click_go_auto()
            else:
                self.__click_go()

            if next_stage:
                time.sleep(2)
                self.check_current_stage(next_stage)
