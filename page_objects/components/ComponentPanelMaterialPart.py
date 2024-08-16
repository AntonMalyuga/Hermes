import testit
from page import Page
from locator import Locator, Input, Select


class ComponentPanelMaterialPart(Page):
    name = 'B2C: Прочие капитальные расходы'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]'
    _LOCATOR_COMPONENT_DROPDOWN_MENU = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//select[@class[contains(., "form-control input-medium input-sm change-expenses-monitoring-object")]]'
    _LOCATOR_COMPONENT_OTHER_CAPITAL_COSTS_DROPDOWN = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//div[@id[contains(., "component-otherCapex")]]/div[1]'
    _LOCATOR_OTHER_CAPITAL_EDIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//div[@id[contains(., "component-otherCapex")]]//i[@class = "fas fa-edit"]'
    _LOCATOR_COMPONENT_DELETE_STRING = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title= "Удалить"]'
    _LOCATOR_COMPONENT_ADD_STRING = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title= "Добавить строку"]'
    _LOCATOR_COMPONENT_ADD_EXPENCE_NAME = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//td[@data-field = "name"]//input[@class = "form-control input-sm"]'
    _LOCATOR_COMPONENT_OBJECT_DROPDOWN = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//select[@class[contains(., "form-control input-sm js--other-capexes-changeOrder")]]'
    _LOCATOR_COMPONENT_ADD_COST = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//td[@data-field = "cost"]//input[@class = "form-control input-sm"]'
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Затратная часть")]/ancestor::div[2]//button[@title = "Сохранить прочие капитальные расходы"]'

    @classmethod
    def fill_drop_down_menu(cls, value):
        with testit.step(f'Заполнить выпадающую форму со значением "{value}"'):
            Select(cls._LOCATOR_COMPONENT_DROPDOWN_MENU).option(value)

    @classmethod
    def push_open_capital_dropdown(cls):
        with testit.step(f'Нажать кнопку открытия выпадающего меню капитальных затрат'):
            Locator(cls._LOCATOR_COMPONENT_OTHER_CAPITAL_COSTS_DROPDOWN).click()

    @classmethod
    def push_other_capital_edit_button(cls):
        with testit.step(f'Нажать кнопку открытия выпадающего меню'):
            Locator(cls._LOCATOR_OTHER_CAPITAL_EDIT_BUTTON).click()

    @classmethod
    def check_new_string_necessity(cls):
        with testit.step(f'Проверить необходимость создания новой формы'):
            Locator(cls._LOCATOR_COMPONENT_DELETE_STRING).is_on_page()

    @classmethod
    def fill_object_dropdown(cls, text):
        with testit.step(f'Заполнить выпадающую форму со значением "{text}"'):
            Select(cls._LOCATOR_COMPONENT_OBJECT_DROPDOWN).option(text)

    @classmethod
    def fill_expence_name(cls, name):
        with testit.step(f'Заполнить статью расхода "{name}"'):
            Input(cls._LOCATOR_COMPONENT_ADD_EXPENCE_NAME).input(name)

    @classmethod
    def fill_cost(cls, cost):
        with testit.step(f'Заполнить стоимость "{cost}"'):
            Input(cls._LOCATOR_COMPONENT_ADD_COST).input(cost)

    @classmethod
    def submit_button_click(cls):
        with testit.step(f'Нажать кнопку сохранения', 'Кнопка нажата'):
            Locator(cls._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    @classmethod
    def add_material_part(cls, value: str, name: str, cost: int, text: str):
        with testit.step(
                f'Добавить материальную часть со значением "{value}", названием расхода "{name}", стоимостью "{cost}"'):
            cls.fill_drop_down_menu(value)
            cls.push_open_capital_dropdown()
            cls.push_other_capital_edit_button()
            cls.check_new_string_necessity()
            cls.fill_object_dropdown(text)
            cls.fill_expence_name(name)
            cls.fill_cost(cost)
            cls.submit_button_click()
