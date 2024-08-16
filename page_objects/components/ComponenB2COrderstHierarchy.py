from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentB2COrdersHierarchy(Page):
    name = 'B2C: Иерархия заявок'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Иерархия заявок")]/ancestor::div[2]'
    _LOCATOR_LINK_PROJECT = f'{_GROUP}//tbody//td[2]/a'
    _LOCATOR_LINK_SMR = f'{_GROUP}//tbody//td[3]/a'
    _LOCATOR_LINK_HOZ = f'{_GROUP}//tbody//td[4]/a'
    _LOCATOR_LINK_GPH = f'{_GROUP}//tbody//td[5]/a'
    _LOCATOR_LINK_CUSTOMER = f'{_GROUP}//tbody//td[6]/a'
    _LOCATOR_LINK_CUSTOMER_ORDER = f'{_GROUP}//tbody//td[7]/a'

    @classmethod
    def get_smr_number(cls, position: int = 0):
        with testit.step(f'Получить номер заявки СМР по позиции "{position}"'):
            return Locator(cls._LOCATOR_LINK_SMR).all[position].text

    @classmethod
    def get_project_number(cls, position: int = 0):
        with testit.step(f'Получить номер проекта "{position}"'):
            return Locator(cls._LOCATOR_LINK_PROJECT).all[position].text

    @classmethod
    def get_gph_number(cls, position: int = 0) -> int:
        with testit.step(f'Получить номер ГПХ "{position}"'):
            return int(Locator(cls._LOCATOR_LINK_GPH).all[position].text)

    @classmethod
    def get_hoz_number(cls, position: int = 0) -> int:
        with testit.step(f'Получить ХОЗ номер "{position}"'):
            return int(Locator(cls._LOCATOR_LINK_HOZ).all[position].text)

    @classmethod
    def get_customer_number(cls, position: int = 0) -> int:
        with testit.step(f'Получить номер подрядчика "{position}"'):
            return int(Locator(cls._LOCATOR_LINK_CUSTOMER).all[position].text)

    @classmethod
    def get_customer_order_number(cls, position: int = 0) -> int:
        with testit.step(f'Получить номер заказа подрядчика "{position}"'):
            return int(Locator(cls._LOCATOR_LINK_CUSTOMER_ORDER).all[position].text)
