from page import Page
from locator import Locator, Input, Select
import testit


class ComponentTypeProject(Page):
    name = 'B2C: Инвестиционный проект'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]'
    _LOCATOR_EDIT_FORM_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "agg-container--limited-height"]//a[@title = "Редактировать"]'
    _LOCATOR_SELECT_TYPE_FIELD = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//select[@name = "project_type"]'
    _LOCATOR_SELECT_TYPE_SUBMIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "input-group-btn"]//button[@type = "submit"]'

    @classmethod
    def push_edit_form_button(cls):
        with testit.step(f'Открыть форму редактирования'):
            Locator(cls._LOCATOR_EDIT_FORM_BUTTON).click()

    @classmethod
    def fill_select_type_field(cls, value):
        with testit.step(f'Заполнить селектовую форму со значением нового типа проекта "{value}"'):
            Select(cls._LOCATOR_SELECT_TYPE_FIELD).option(value)

    @classmethod
    def push_submit_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_SELECT_TYPE_SUBMIT_BUTTON).click()

    @classmethod
    def change_type_project(cls, value: str):
        with testit.step(f'Изменить тип проекта на тип "{value}"'):
            cls.push_edit_form_button()
            cls.fill_select_type_field(value)
            cls.push_submit_button()
