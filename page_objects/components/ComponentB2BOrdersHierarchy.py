import testit
from dataclasses import dataclass, field
from page import Page
from locator import Locator, Select, Input


class ComponentB2BOrdersHierarchy:
    name = 'B2B: Иерархия заявок'
    group = 'Иерархия заявок'

    _SELECTOR_GROUP = f'//div[@class="panel panel-material"]//span[contains(., "{group}")]/ancestor::div[2]'
    _LOCATOR_LINK_PROJECT = f'{_SELECTOR_GROUP}//tbody//td[1]/a'
    _LOCATOR_LINK_CLIENT = f'{_SELECTOR_GROUP}//tbody//td[2]/a'
    _LOCATOR_LINK_CONSTRUCT = f'{_SELECTOR_GROUP}//tbody//td[3]/a'
    _LOCATOR_LINK_SMU = f'{_SELECTOR_GROUP}//tbody//td[4]/a'
    _LOCATOR_LINK_HOZ = f'{_SELECTOR_GROUP}//tbody//td[5]/a'
    _LOCATOR_LINK_GPH = f'{_SELECTOR_GROUP}//tbody//td[6]/a'
    _LOCATOR_LINK_CUSTOMER = f'{_SELECTOR_GROUP}//tbody//td[7]/a'
    _LOCATOR_LINK_VTR = f'{_SELECTOR_GROUP}//tbody//td[8]/a'

    @classmethod
    def get_project_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_PROJECT)
        with testit.step(f'Получить номер клиентского проекта: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_client_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_CLIENT)
        with testit.step(f'Получить номер клиентской заявки: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_construct_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_CONSTRUCT)
        with testit.step(f'Получить номер строительной заявки: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_smu_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_SMU)
        with testit.step(f'Получить номер заявки СМУ: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_hoz_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_HOZ)
        with testit.step(f'Получить номер заявки хоз. способ: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_gph_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_GPH)
        with testit.step(f'Получить номер заявки ГПХ: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_customer_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_CUSTOMER)
        with testit.step(f'Получить номер заявки договора: "{element.text}"'):
            return int(element.text)

    @classmethod
    def get_vtr_number(cls) -> int:
        element = Locator(cls._LOCATOR_LINK_VTR)
        with testit.step(f'Получить номер заявки ВТР: "{element.text}"'):
            return int(element.text)
