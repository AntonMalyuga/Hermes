import testit
import time
from driver import Driver
from locator import Locator


class Page:
    """
    Main class for pages, contains locators
    """

    BASE_PAGE_URL = 'https://hermes-test.rt.ru/'
    path = ''
    _LOCATOR_RELOAD_PAGE = '//div[@class="h-loader"]'

    @classmethod
    def wait_reload_page(cls, time_wait: int = 2):
        Locator(cls._LOCATOR_RELOAD_PAGE).wait_attached()
        time.sleep(time_wait)

    def open(self):
        with testit.step(f'Открыть ссылку: {self.BASE_PAGE_URL}'):
            testit.addLinks(url=f'{Page().BASE_PAGE_URL}', title='Страница')
            Driver().page.goto(self.BASE_PAGE_URL)
            return self

    @classmethod
    def open_with_path(cls, path: str):
        with testit.step(f'Открыть ссылку: {cls.BASE_PAGE_URL}{path}'):
            testit.addLinks(url=f'{Page().BASE_PAGE_URL}{path}', title='Страница')
            Driver().page.goto(cls.BASE_PAGE_URL + path)
            return cls

    @classmethod
    def open_by_default(cls):
        with testit.step(f'Открыть ссылку: {Page().BASE_PAGE_URL}{cls.path}'):
            testit.addLinks(url=f'{Page().BASE_PAGE_URL}{cls.path}', title='Страница')
            Driver().page.goto(Page().BASE_PAGE_URL + cls.path)

    @staticmethod
    def current_url() -> str:
        return Driver().page.url
