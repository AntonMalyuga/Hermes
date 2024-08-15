import time

import testit
from page import Page
from locator import Locator, Select


class ComponentCheckListWiFi(Page):
    name = 'B2C: WiFi'

    GROUP = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]'
    _LOCATOR_COMPONENT_COLLAPSED_MENU = f'{GROUP}//div[contains(@data-target, "collapseChecklist-wifi")]'
    _LOCATOR_COMPONENT_EDIT_BUTTON = f'{GROUP}//form[contains(@action, "/b2c/checklist/save/wifi")]//button[@title="Редактировать"]'
    _LOCATOR_COMPONENT_SELECT_ITEM = f'{GROUP}//form[@class = "form-horizontal js--load-element"]//label[text() = "Статья затрат"]/ancestor::div[1]//select[@class = "form-control input-sm"]'
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = f'{GROUP}//div[@id[contains(., "collapseChecklist-wifi")]]//div[@class = "btn-group btn-group-sm"]//button[@class = "btn btn-primary"]'

    @classmethod
    def open_drop_down_panel(cls):
        with testit.step(f'Открыть выпадающую панель'):
            Locator(cls._LOCATOR_COMPONENT_COLLAPSED_MENU).click()

    @classmethod
    def push_edit_button(cls):
        with testit.step(f'Нажать кнопку редактирования'):
            Locator(cls._LOCATOR_COMPONENT_EDIT_BUTTON).click()

    @classmethod
    def select_dropdown_panel(cls, value):
        with testit.step(f'Выбрать значение в выпадающем меню "{value}"'):
            Select(cls._LOCATOR_COMPONENT_SELECT_ITEM).option(value)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    @classmethod
    def add_cost_wifi(cls, value: str):
        with testit.step(f'Добавить стоимость услуги wi-fi "{value}"'):
            cls.open_drop_down_panel()
            cls.push_edit_button()
            cls.select_dropdown_panel(value)
            cls.push_submit_button()
