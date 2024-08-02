import testit
import time
from driver import Driver
from locator import Locator


class Page:
    path = ''

    _LOCATOR_RELOAD_PAGE = '//div[@class="h-loader"]'
    _BTN_CLOSE_CURRENT_TAB = '//ul[contains(@class,"nav-tabs")]/li[@class="active"]//button'

    @classmethod
    def wait_reload_page(cls, time_wait: int = 2):
        Locator(cls._LOCATOR_RELOAD_PAGE).wait_attached()
        time.sleep(time_wait)

    def open(self):
        with testit.step(f'Открыть ссылку: {self.get_base_url()}'):
            testit.addLinks(url=f'{Page().get_base_url()}', title='Страница')
            Driver().page.goto(self.get_base_url())
            return self

    @classmethod
    def open_with_path(cls, path: str):
        with testit.step(f'Открыть ссылку: {cls.get_base_url()}{path}'):
            testit.addLinks(url=f'{Page().get_base_url()}{path}', title='Страница')
            Driver().page.goto(cls.get_base_url() + path)
            return cls

    @classmethod
    def open_by_default(cls):
        with testit.step(f'Открыть ссылку: {Page().get_base_url()}{cls.path}'):
            testit.addLinks(url=f'{Page().get_base_url()}{cls.path}', title='Страница')
            Driver().page.goto(cls.get_base_url() + cls.path)

    @classmethod
    def get_base_url(cls) -> str:
        return Driver().url

    @staticmethod
    def current_url() -> str:
        return Driver().page.url

    @classmethod
    def close_current_tab(cls):
        Locator(cls._BTN_CLOSE_CURRENT_TAB).click()
