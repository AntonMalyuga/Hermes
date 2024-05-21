from selenium.webdriver.common.by import By
import testit


class ComponentB2BOrdersHierarchy:
    name = 'B2B: Иерархия заявок'
    group = 'Иерархия заявок'

    _SELECTOR_GROUP = f'//div[@class="panel panel-material"]//span[contains(., "{group}")]/ancestor::div[2]'
    _LOCATOR_LINK_PROJECT = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[1]/a')
    _LOCATOR_LINK_CLIENT = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[2]/a')
    _LOCATOR_LINK_CONSTRUCT = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[3]/a')
    _LOCATOR_LINK_SMU = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[4]/a')
    _LOCATOR_LINK_HOZ = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[5]/a')
    _LOCATOR_LINK_GPH = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[6]/a')
    _LOCATOR_LINK_CUSTOMER = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[7]/a')
    _LOCATOR_LINK_VTR = (By.XPATH, f'{_SELECTOR_GROUP}//tbody//td[8]/a')

    def move_to_group(self):
        self.move_to_element((By.XPATH, self._SELECTOR_GROUP))

    def get_project_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_PROJECT)
        with testit.step(f'Получить номер клиентского проекта: "{element.text}"'):
            return int(element.text)

    def get_client_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_CLIENT)
        with testit.step(f'Получить номер клиентской заявки: "{element.text}"'):
            return int(element.text)

    def get_construct_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_CONSTRUCT)
        with testit.step(f'Получить номер строительной заявки: "{element.text}"'):
            return int(element.text)

    def get_smu_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_SMU)
        with testit.step(f'Получить номер заявки СМУ: "{element.text}"'):
            return int(element.text)

    def get_hoz_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_HOZ)
        with testit.step(f'Получить номер заявки хоз. способ: "{element.text}"'):
            return int(element.text)

    def get_gph_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_GPH)
        with testit.step(f'Получить номер заявки ГПХ: "{element.text}"'):
            return int(element.text)

    def get_customer_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_CUSTOMER)
        with testit.step(f'Получить номер заявки договора: "{element.text}"'):
            return int(element.text)

    def get_vtr_number(self) -> int:
        self.move_to_group()
        element = self.find_element(self._LOCATOR_LINK_VTR)
        with testit.step(f'Получить номер заявки ВТР: "{element.text}"'):
            return int(element.text)
