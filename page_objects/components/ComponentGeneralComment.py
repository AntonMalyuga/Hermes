import time
from page import Page
from locator import Locator, Input, Select
import testit


class ComponentGeneralComment(Page):
    name = 'B2B: Общий комментарии'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_CURRENT_COMMENT = f'{_GROUP}//div[contains(text(), "Комментарий к заявке")]/following::div[1]//span'
    _LOCATOR_BTN_OPEN_EDITOR = f'{_GROUP}//a[contains(@href, "ExtractComment")]//i'
    _LOCATOR_AREA_COMMENT = f'{_GROUP}//form[contains(@action,"Comment")]//textarea'
    _LOCATOR_BTN_SAVE_COMMENT = f'{_GROUP}//form[contains(@action,"Comment")]//button'
    _LOCATOR_BTN_CANCEL_EDIT = f'{_GROUP}//form[contains(@action,"Comment")]//a'

    @classmethod
    def get_current_comment(cls) -> str:
        group_name = Locator(cls._LOCATOR_CURRENT_COMMENT).text
        with testit.step(f'Получить текущее имя группы проекта {group_name}'):
            return group_name

    @classmethod
    def open_editor(cls):
        with testit.step('Открыть редактор комментария'):
            Locator(cls._LOCATOR_BTN_OPEN_EDITOR).click()

    @classmethod
    def set_comment(cls, comment: str):
        with testit.step(f'Заполнить комментарий на {comment}'):
            Input(cls._LOCATOR_AREA_COMMENT).input(comment)

    @classmethod
    def save_comment(cls):
        with testit.step('Сохранить комментарий'):
            Locator(cls._LOCATOR_BTN_SAVE_COMMENT).click()

    @classmethod
    def cancel_edit(cls):
        with testit.step('Отменить изменения комментария'):
            Locator(cls._LOCATOR_BTN_CANCEL_EDIT).click()
