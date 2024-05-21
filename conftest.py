import pytest
from driver import Driver


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser', '-B',
#         default='firefox',
#         choices=('chrome', 'firefox'),
#         help='Выбирает необходимый драйвер для работы с браузером, по умолчанию Firefox'
#     )
#     parser.addoption(
#         '--url', '-U',
#         default='https://hermes-test.rt.ru/',
#         choices=(
#             'https://hermes-test.rt.ru/',
#             'http://hermes-pp.rt.ru/',
#             'https://hermes-prod.rt.ru/',
#             'http://hermes-beta.rt.ru',
#             'https://hermes-gamma.rt.ru/'
#         ),
#         help='Выбирает среду для запуска тестов, по умолчанию тест'
#     )
#     parser.addoption(
#         '--headless',
#         default=False,
#         choices=(True, False),
#         help='Запускает фоновый режим автотестов'
#     )
#
#
# @pytest.fixture()
# def base_url(request):
#     return request.config.getoption('--url')
#
#
# @pytest.fixture(autouse=True)
# def browser(request, base_url) -> dr:
#     options = Options()
#
#     if request.config.getoption('--headless'):
#         options.add_argument('--headless')
#
#     options.add_argument('--disable-dev-shm-usage')
#
#     driver = dr(service=Service(ChromeDriverManager().install()), options=options)
#     driver.maximize_window()
#
#     request.addfinalizer(driver.quit)
#     driver.get(url=base_url)
#
#     return driver

def is_mobile(request) -> bool:
    markers = request.node.own_markers
    if [mark for mark in markers if mark.name.lower() == 'mobile']:
        return True
    else:
        return False


def driver(request):
    mobile = is_mobile(request=request)
    webdriver = Driver(mobile=mobile)

    yield webdriver

    try:
        webdriver.quit()
    finally:
        webdriver.__class__._instances = {}
