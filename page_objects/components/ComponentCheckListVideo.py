import time
import testit
from page import Page
from locator import Locator, Select, Input


class ComponentCheckListVideo(Page):
    name = 'B2C: Видеонаблюдение'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]'
    _LOCATOR_COMPONENT_COLLAPSED_MENU = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//b[text()="Видеонаблюдение"]/ancestor::div[2]//div[@class = "panel-heading pointer"]'
    _LOCATOR_COMPONENT_EDIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//form[@action = "https://hermes-test.rt.ru/b2c/checklist/save/cctv"]//button[@class = "btn btn-info js--b2c-checklist-form-editor"]'
    _LOCATOR_COMPONENT_SELECT_ITEM = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//b[text()="Видеонаблюдение"]/ancestor::div[2]//select[@class = "form-control input-sm"]'
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]//div[@id[contains(., "collapseChecklist-cctv")]]//div[@class = "btn-group btn-group-sm"]//button[@class = "btn btn-primary"]'

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
            select = Select(cls._LOCATOR_COMPONENT_SELECT_ITEM).option(value)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    @classmethod
    def add_cost_video(cls, value: str):
        with testit.step(f'Добавить стоимость услуги видеосвязи "{value}"'):
            cls.open_drop_down_panel()
            cls.push_edit_button()
            cls.select_dropdown_panel(value)
            cls.push_submit_button()
