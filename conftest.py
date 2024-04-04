import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        '--browser', '-B',
        default='chrome',
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

    def get_driver_by_windows():
        if browser == 'chrome':
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == 'firefox':
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f'Браузер {browser} не поддерживается')

    def get_driver_by_linux():
        if browser == 'chrome':
            options = Options()
            options.add_argument('--disable-dev-shm-usage')
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:
            raise ValueError(f'Браузер {browser} не поддерживается')

    if os.name == 'posix':
        driver = get_driver_by_linux()
    else:
        driver = get_driver_by_windows()

    request.addfinalizer(driver.quit)

    def open(path=''):
        return driver.get(base_url + path)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.open = open
    driver.open()

    driver.base_url = base_url

    return driver
