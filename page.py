from driver import Driver
import testit

# class BasePage:
#
#     @staticmethod
#     def open_page(path: str, title_test_it: str = ''):
#         path = f'{Driver().current_url}{path}'
#         # with testit.addLink(url=path, title=title_test_it):
#         Driver().get(path)
#
#     @staticmethod
#     def current_url() -> str:
#         return Driver().current_url


from driver import Driver


class Page:
    """
    Main class for pages, contains locators
    """

    BASE_PAGE_URL = 'https://hermes-test.rt.ru/'
    path = ''

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
