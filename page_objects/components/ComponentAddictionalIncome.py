import time

from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentAdditionalIncome(Page):
    name = 'B2C: Дополнительные доходы'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]'
    _LOCATOR_EDIT_FORM_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@title = "Редактировать дополнительные доходы"]'
    _LOCATOR_TABLE_ROWS = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//form[@action[contains(., "additionalIncome")]]//table[@class="b2c-table-component"]/tbody/tr'
    _LOCATOR_DELETE_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//button[@title = "Удалить доход"]'
    _LOCATOR_CREATE_NEW_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@class = "btn btn-default js--b2c-components-add-row"]'
    _LOCATOR_ADD_NAME_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//input[@class = "form-control input-sm"]'
    _LOCATOR_ADD_INFRASTRUCTURE_TYPE_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//select[@class = "form-control input-sm js--fetch-income-types-for-infrastructure"]'
    _LOCATOR_ADD_INCOME_TYPE_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//td[@class[contains(., "column")]]//select[@class = "form-control input-sm"]'
    _LOCATOR_ADD_ABONENT_BASE_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//select[contains(@name, "subscriberBaseType[1]") ]'
    _LOCATOR_ADD_YEARS_STRING = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//tr[@class[not(contains(., "new-income"))]]//input[@class = "form-control input-sm js--b2c-year-value"]'
    _LOCATOR_SAVE_BUTTON = '//div[@class="panel panel-material"]//span[contains(., "Проектные параметры")]/ancestor::div[2]//button[@class = "btn btn-primary"]'

    @classmethod
    def push_edit_form_button(cls):
        with testit.step(f'Нажать кнопку редактирования формы', 'Кнопка редактирования формы нажата'):
            Locator(cls._LOCATOR_EDIT_FORM_BUTTON).click()

    @classmethod
    def check_new_string_necessity(cls):
        with testit.step(f'Проверить необходимость создания нового поля'):
            elements = Locator(cls._LOCATOR_TABLE_ROWS).all
            if len(elements) > 1:
                Locator(cls._LOCATOR_DELETE_STRING).click()
                Locator(cls._LOCATOR_CREATE_NEW_STRING).click()
            else:
                Locator(cls._LOCATOR_CREATE_NEW_STRING).click()

    @classmethod
    def fill_name_string(cls, name):
        with testit.step(f'Заполнить имя поля "{name}"'):
            cls.find_element(cls._LOCATOR_ADD_NAME_STRING).send_keys(name)

    @classmethod
    def fill_infrastructure_string(cls, infrastructure_type):
        with testit.step(f'Заполнить поле инфраструктуры "{infrastructure_type}"'):
            Select(cls._LOCATOR_ADD_INFRASTRUCTURE_TYPE_STRING).option(infrastructure_type)

    @classmethod
    def fill_income_string(cls, income_type):
        with testit.step(f'Заполнить поле доходов "{income_type}"'):
            Select(cls._LOCATOR_ADD_INCOME_TYPE_STRING).option(income_type)

    @classmethod
    def fill_abonent_string(cls, abonent_type):
        with testit.step(f'Заполнить абонента "{abonent_type}"'):
            Select(cls._LOCATOR_ADD_ABONENT_BASE_STRING).option(abonent_type)

    @classmethod
    def fill_years_income(cls, value):
        with testit.step(f'Заполнить поле доходов за год"{value}"'):
            elements = Locator(cls._LOCATOR_ADD_YEARS_STRING).all

        for element in elements:
            element.fill(value)
            time.sleep(1)

    @classmethod
    def push_save_button(cls):
        with testit.step(f'Нажать кнопку сохранения'):
            Locator(cls._LOCATOR_SAVE_BUTTON).click()

    @classmethod
    def add_addictional_income(cls, name: str, infrastructure_type: str, income_type: str, abonent_type: str,
                               value: int):
        with testit.step(
                f'Добавить в поле доп.доходов: тип инфрастуктуры "{infrastructure_type}", тип дохода "{income_type}", тип абонента "{abonent_type}", значение"{value}", название "{name}"'):
            cls.push_edit_form_button()
            cls.check_new_string_necessity()
            cls.fill_name_string(name)
            cls.fill_infrastructure_string(infrastructure_type)
            cls.fill_income_string(income_type)
            cls.fill_abonent_string(abonent_type)
            cls.fill_years_income(value)
            cls.push_save_button()
