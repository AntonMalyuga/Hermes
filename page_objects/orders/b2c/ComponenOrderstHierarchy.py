from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
from selenium.webdriver.common.keys import Keys
import random


class ComponentNaturalIndicator(Order):
    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Иерархия заявок")]/ancestor::div[2]'
    _LOCATOR_LINK_PROJECT = (By.XPATH, f'{_GROUP}//tbody//td[2]/a')
    _LOCATOR_LINK_SMR = (By.XPATH, f'{_GROUP}//tbody//td[3]/a')
    _LOCATOR_LINK_HOZ = (By.XPATH, f'{_GROUP}//tbody//td[4]/a')
    _LOCATOR_LINK_GPH = (By.XPATH, f'{_GROUP}//tbody//td[5]/a')
    _LOCATOR_LINK_CUSTOMER = (By.XPATH, f'{_GROUP}//tbody//td[5]/a')

    def move_to_group(self):
        self.move_to_element((By.XPATH, self._GROUP))

    def get_smr_number(self, position: int = 0):
        self.move_to_group()
        return self.find_elements(self._LOCATOR_LINK_SMR)[position].text

    def get_project_number(self, position: int = 0):
        self.move_to_group()
        return self.find_elements(self._LOCATOR_LINK_PROJECT)[position].text

    def get_gph_number(self, position: int = 0) -> int:
        self.move_to_group()
        return int(self.find_elements(self._LOCATOR_LINK_GPH)[position].text)

    def get_hoz_number(self, position: int = 0):
        self.move_to_group()
        return self.find_elements(self._LOCATOR_LINK_HOZ)[position].text

    def get_customer_number(self, position: int = 0):
        self.move_to_group()
        return self.find_elements(self._LOCATOR_LINK_CUSTOMER)[position].text
