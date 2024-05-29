import time

import testit
from locator import Locator, Input, Select
from page import Page


class ComponentCloseStage(Page):
    name = 'Управление этапом'

    _LOCATOR_FORM_CLOSE_STAGE_PASS = '//select[@name="passDescriptionId"]'
    _LOCATOR_FORM_CLOSE_STAGE_REASON = '//select[contains(@name,"reasonId")]'
    _LOCATOR_FORM_CLOSE_STAGE_COMMENT = '//div[contains(@id, "transitionComment")]/textarea'
    _LOCATOR_FORM_BUTTON_MANUAL_CLOSE_STAGE = '//div[contains(@id, "moveOrderSelector")]//button[text()="Перейти"]'
    _LOCATOR_FORM_TEXT_NEXT_STAGE = '//form[@id="close_stage_form"]//div[contains(@id, "comment")]/div[1]'
    _LOCATOR_FORM_BUTTON_AUTO_CLOSE_STAGE = '//div[contains(@id, "moveOrderSelector")]//button[contains(text(), "Перейти без проверок")]'
    _LOCATOR_ALERT_FOR_PASS = '//div[@class="text-danger mt-10" and @id="required-actions"]'

    @classmethod
    def _set_manual_pass(cls, pass_name: str):
        with testit.step(f'Выбрать ручной переход: {pass_name}'):
            Select(cls._LOCATOR_FORM_CLOSE_STAGE_PASS).option(pass_name)

    @classmethod
    def _set_reason(cls, reason: str):
        with (testit.step(f'Установить причину: "{reason}"')):
            Locator(cls._LOCATOR_FORM_CLOSE_STAGE_REASON).wait_for_displayed()
            Select(cls._LOCATOR_FORM_CLOSE_STAGE_REASON).ajax_option(reason)

    @classmethod
    def _set_comment(cls, comment: str):
        with testit.step(f'Установить комментарий: "{comment}"'):
            Input(cls._LOCATOR_FORM_CLOSE_STAGE_COMMENT).input(comment)
            Locator(cls._LOCATOR_FORM_CLOSE_STAGE_COMMENT).press_sequentially(' ')
            Locator(cls._LOCATOR_FORM_CLOSE_STAGE_COMMENT).press('Backspace')

    @classmethod
    def _get_name_next_stage(cls) -> str:
        next_stage = Locator(cls._LOCATOR_FORM_TEXT_NEXT_STAGE).text
        next_stage = next_stage.replace('»', '')
        next_stage = next_stage.split('«')[1]
        with testit.step(f'Получить имя следующего этапа: {next_stage}'):
            return next_stage

    @classmethod
    def _click_go(cls):
        with testit.step('Нажать "Перейти"'):
            Locator(cls._LOCATOR_FORM_BUTTON_MANUAL_CLOSE_STAGE).click()

    @classmethod
    def get_text_alert_for_pass(cls) -> str:
        alert_text = Locator(cls._LOCATOR_ALERT_FOR_PASS).text
        with testit.step(f'Установить комментарий: "{alert_text}"'):
            return alert_text

    @classmethod
    def check_show_alert_for_pass(cls) -> bool:
        with testit.step(f'Проверить отображение ошибки проверки на переходе'):
            if Locator(cls._LOCATOR_ALERT_FOR_PASS).text != '':
                return True
            else:
                return False

    @classmethod
    def close_stage(
            cls,
            pass_name: str,
            next_stage: str = '',
            reason: str = '',
            comment: str = '',
            is_go: bool = True,
            is_auto: bool = False

    ):
        with testit.step(f'Закрыть переход'):

            cls._set_manual_pass(pass_name)
            time.sleep(2)

            if reason != '':
                cls._set_reason(reason)

            if comment != '':
                cls._set_comment(comment)

            if is_go:
                time.sleep(2)
                if is_auto:
                    cls._click_go_auto()
                else:
                    cls._click_go()

            if next_stage != '':
                cls.check_next_stage(next_stage)

    @classmethod
    def _click_go_auto(cls):
        with testit.step('Нажать "Перейти без проверок"'):
            Locator(cls._LOCATOR_FORM_BUTTON_AUTO_CLOSE_STAGE).click()

    @classmethod
    def check_next_stage(cls, next_stage):
        with testit.step(f'Проверить имя следующего этапа: {next_stage}'):
            if cls._get_name_next_stage() == next_stage:
                return True
            else:
                return False
