import time
import testit
from locator import Locator, Input, Select
from page import Page


class Order(Page):
    id = ''
    name = ''
    path = 'aggregator'

    _LOCATOR_TAB = '//div[@class="tab-content"]//title'
    _LOCATOR_ORDER_ID = '//div[text()="Номер заявки:"]/following::div[1]'
    _LOCATOR_STAGE_NAME = '//div[text()= "Текущий этап и время начала:"]/following::div[1]'
    _LOCATOR_RELOAD_PAGE = '//div[@class="h-loader"]'

    @classmethod
    def open_order(cls, order: int):
        cls.open_with_path(path=f'{cls.path}/{order}')

    @classmethod
    def get_tab_name(cls) -> str:
        return Locator(cls._LOCATOR_TAB).text

    @classmethod
    def get_order_id(cls) -> int:
        order_id = int(Locator(cls._LOCATOR_ORDER_ID).text)
        with testit.step(f'Получить номер заявки: {order_id}'):
            return order_id

    @classmethod
    def get_current_stage(cls) -> str:
        stage_name = Locator(cls._LOCATOR_STAGE_NAME).text
        stage_name = stage_name.replace('«', '')
        return stage_name.split('»')[0]

    @classmethod
    def wait_reload_page(cls, time_wait: int = 2):
        Locator(cls._LOCATOR_RELOAD_PAGE).wait_attached()
        time.sleep(time_wait)
