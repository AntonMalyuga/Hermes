import testit
from page import Page
from locator import Locator, Select, Input


class ComponentControlDate(Page):
    name = 'B2C: Контрольные даты'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Контрольные даты")]/ancestor::div[2]'
    _LOCATOR_BUTTON_CHANGE_ALL_CONTROL_DATES = '//div[@id[contains(., "btn-editor-control-dates")]]'

    @classmethod
    def change_all_control_dates(cls, cnt_dates: int):
        with testit.step(f'Изменить контрольные даты "{cnt_dates}"'):
            component = cls._LOCATOR_BUTTON_CHANGE_ALL_CONTROL_DATES
            Locator(f'{component}//button[@class[contains(., "btn-default")]]').click()
            Input(f'//div[@id[contains(., "editor-control-dates")]]//input[@type="text"]').input(str(cnt_dates))
            Locator(f'//div[@id[contains(., "editor-control-dates")]]//button[@type="submit"]').click()
