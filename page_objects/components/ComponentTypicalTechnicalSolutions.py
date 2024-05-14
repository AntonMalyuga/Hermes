import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order


class ComponentTypicalTechnicalSolutions(Order):

    name = 'B2B: Типовые технические решения'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Капитальные расходы")]/ancestor::div[2]'
    _LOCATOR_GROUP = (By.XPATH, _GROUP)
    _LOCATOR_A_EDIT = (By.XPATH, f'{_GROUP}//a[contains(@href,"TypicalSolution") and @title="Редактировать"]')
    _LOCATOR_SELECT_LIST_TYPE_TECHNICAL_SOLUTIONS = (
    By.XPATH, f'{_GROUP}//select[@name="typicalSolutionId"]/following::div[1]')
    _LOCATOR_BTN_SAVE_TECHNICAL_SOLUTION = (
    By.XPATH, f'{_GROUP}//form[contains(@action,"ChangeTypicalSolution")]//button[contains(text(), "Изменить")]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def open_editor(self):
        self.find_element(self._LOCATOR_A_EDIT).click()

    def change_typical_technical_solutions(self, type_technical_solutions: str):
        select = self.find_element(self._LOCATOR_SELECT_LIST_TYPE_TECHNICAL_SOLUTIONS)
        select.click()
        select.find_element(By.XPATH, f'//span[text()="{type_technical_solutions}"]').click()

    def save_typical_technical_solutions(self):
        self.find_element(self._LOCATOR_BTN_SAVE_TECHNICAL_SOLUTION).click()

    def set_typical_technical_solutions(self, type_technical_solutions: str):
        self.move_to_group()
        self.open_editor()
        self.change_typical_technical_solutions(type_technical_solutions=type_technical_solutions)
        self.save_typical_technical_solutions()
