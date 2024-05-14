from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select
import testit


class ComponentTypeProject(Order):

    name = 'B2C: Инвестиционный проект'

    _LOCATOR_GROUP = (
        By.XPATH, '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]')
    _LOCATOR_EDIT_FORM_BUTTON = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "agg-container--limited-height"]//a[@title = "Редактировать"]')
    _LOCATOR_SELECT_TYPE_FIELD = (By.XPATH,
                                  '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//select[@name = "project_type"]')
    _LOCATOR_SELECT_TYPE_SUBMIT_BUTTON = (By.XPATH,
                                          '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]//div[@class = "input-group-btn"]//button[@type = "submit"]')

    def push_edit_form_button(self):
        with testit.step(f'Открыть форму редактирования'):
            self.find_element(locator=self._LOCATOR_EDIT_FORM_BUTTON).click()

    def fill_select_type_field(self, value):
        with testit.step(f'Заполнить селектовую форму со значением нового типа проекта "{value}"'):
            select = Select(self.find_element(locator=self._LOCATOR_SELECT_TYPE_FIELD))
            select.select_by_visible_text(value)

    def push_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения'):
            self.find_element(locator=self._LOCATOR_SELECT_TYPE_SUBMIT_BUTTON).click()

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    def change_type_project(self, value: str):
        with testit.step(f'Изменить тип проекта на тип "{value}"'):
            self.check_loader()
            self.move_to_group()
            self.push_edit_form_button()
            self.fill_select_type_field(value)
            self.push_submit_button()
