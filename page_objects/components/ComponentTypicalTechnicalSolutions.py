import testit
from page import Page
from locator import Locator, Select, Input


class ComponentTypicalTechnicalSolutions(Page):
    name = 'B2B: Типовые технические решения'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_A_EDIT = f'{_GROUP}//a[contains(@href,"TypicalSolution") and @title="Редактировать"]'
    _LOCATOR_SELECT_LIST_TYPE_TECHNICAL_SOLUTIONS = f'{_GROUP}//select[@name="typicalSolutionId"]/following::div[1]'
    _LOCATOR_BTN_SAVE_TECHNICAL_SOLUTION = f'{_GROUP}//form[contains(@action,"ChangeTypicalSolution")]//button[contains(text(), "Изменить")]'

    @classmethod
    def open_editor(cls):
        Locator(cls._LOCATOR_A_EDIT).click()

    @classmethod
    def change_typical_technical_solutions(cls, type_technical_solutions: str):
        select = Locator(cls._LOCATOR_SELECT_LIST_TYPE_TECHNICAL_SOLUTIONS)
        select.click()
        select.locator(f'//span[text()="{type_technical_solutions}"]').click()

    @classmethod
    def save_typical_technical_solutions(cls):
        Locator(cls._LOCATOR_BTN_SAVE_TECHNICAL_SOLUTION).click()

    @classmethod
    def set_typical_technical_solutions(cls, type_technical_solutions: str):
        cls.open_editor()
        cls.change_typical_technical_solutions(type_technical_solutions=type_technical_solutions)
        cls.save_typical_technical_solutions()
