import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser', '-B',
        default='firefox',
        choices=('chrome', 'firefox'),
        help='Выбирает необходимый драйвер для работы с браузером, по умолчанию Firefox'
    )
    parser.addoption(
        '--url', '-U',
        default='https://hermes-test.rt.ru/',
        choices=(
            'https://hermes-test.rt.ru/',
            'http://hermes-pp.rt.ru/',
            'https://hermes-prod.rt.ru/',
            'http://hermes-beta.rt.ru',
            'https://hermes-gamma.rt.ru/'
        ),
        help='Выбирает среду для запуска тестов, по умолчанию тест'
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def driver(request, base_url):
    browser = request.config.getoption('--browser')

    def connect_by_windows():
        if browser == 'chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f'Браузер {browser} не поддерживается')

    def connect_by_linux():
        if browser == 'chrome':
            driver = webdriver.Firefox('~/Документы/geckodriver')
        else:
            raise ValueError(f'Браузер {browser} не поддерживается')

    request.addfinalizer(driver.quit)

    if os.name == 'posix':
        connect_by_linux()
    else:
        connect_by_windows()

    def open(path=''):
        return driver.get(base_url + path)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.open = open
    driver.open()

    return driver
