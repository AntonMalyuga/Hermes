from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.common.action_chains import ActionChains
import testit


class ComponentCreateProjectButton(Order):

    name = 'B2C: Создать строительный проект'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_CREATE_PROJECT_BUTTON = f'{_GROUP}//a[contains(., "Создать строительный проект")]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.check_loader()
            self.move_to_element(self._GROUP))

    def confirm(self):
        with testit.step(f'Открыть форму создания проекта'):
            self.move_to_group()
            self.find_element(locator=self._LOCATOR_CREATE_PROJECT_BUTTON).click()
