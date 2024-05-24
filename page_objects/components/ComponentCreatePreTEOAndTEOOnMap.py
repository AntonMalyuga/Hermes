from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class ComponentCreatePreTEOAndTEOOnMap(Order):

    name = 'Создание предТЭО и ТЭО на карте'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_OPEN_MAP = f'{_GROUP}//a[contains(., "Создание предТЭО и ТЭО на карте")]')

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.check_loader()
            self.move_to_element(self._GROUP))

    def open_form(self):
        with testit.step(f'Открыть форму создания проекта'):
            self.check_loader()
            self.move_to_group()
            self.find_element(locator=self._LOCATOR_OPEN_MAP).click()
