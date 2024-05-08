import time
import testit
from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.support.select import Select


class ComponentCheckListWiFi(Order):
    GROUP = '//div[@class="panel panel-material"]//span[contains(., "Чек-лист")]/ancestor::div[2]'
    _LOCATOR_COMPONENT_COLLAPSED_MENU = (By.XPATH,
                                         f'{GROUP}/b[text()="Wi-Fi"]/ancestor::div[2]//div[@data-toggle = "collapse"]')
    _LOCATOR_COMPONENT_EDIT_BUTTON = (By.XPATH,
                                      f'{GROUP}//form[contains(@action, "/b2c/checklist/save/wifi")]//button[@title="Редактировать"]')
    _LOCATOR_COMPONENT_SELECT_ITEM = (By.XPATH,
                                      f'{GROUP}//form[@class = "form-horizontal js--load-element"]//label[text() = "Статья затрат"]/ancestor::div[1]//select[@class = "form-control input-sm"]')
    _LOCATOR_COMPONENT_SUBMIT_BUTTON = (By.XPATH,
                                        f'{GROUP}//div[@id[contains(., "collapseChecklist-wifi")]]//div[@class = "btn-group btn-group-sm"]//button[@class = "btn btn-primary"]')

    def open_drop_down_panel(self):
        with testit.step(f'Открыть выпадающую панель'):
            self.find_element(locator=self._LOCATOR_COMPONENT_COLLAPSED_MENU).click()

    def push_edit_button(self):
        with testit.step(f'Нажать кнопку редактирования'):
            self.find_element(locator=self._LOCATOR_COMPONENT_EDIT_BUTTON).click()

    def select_dropdown_panel(self, value):
        with testit.step(f'Выбрать значение в выпадающем меню "{value}"'):
            select = Select(self.find_element(locator=self._LOCATOR_COMPONENT_SELECT_ITEM))
            select.select_by_value(value)

    def push_submit_button(self):
        with testit.step(f'Нажать кнопку сохранения'):
            self.find_element(locator=self._LOCATOR_COMPONENT_SUBMIT_BUTTON).click()

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element((By.XPATH, self.GROUP))

    def add_cost_wifi(self, value: str):
        with testit.step(f'Добавить стоимость услуги wi-fi "{value}"'):
            self.check_loader()
            self.move_to_group()
            self.open_drop_down_panel()
            self.push_edit_button()
            self.select_dropdown_panel(value)
            self.push_submit_button()
