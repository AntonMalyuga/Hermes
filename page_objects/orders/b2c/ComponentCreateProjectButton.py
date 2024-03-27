from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order


class ComponentCreateProjectButton(Order):
    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_CREATE_PROJECT_BUTTON = (By.XPATH, f'{_GROUP}//a[contains(., "Создать строительный проект")]')

    def move_to_group(self):
        self.check_loader()
        self.move_to_element((By.XPATH, self._GROUP))

    def confirm(self):
        self.move_to_group()
        self.find_element(locator=self._LOCATOR_CREATE_PROJECT_BUTTON).click()
