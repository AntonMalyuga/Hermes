import pytest
from driver import Driver
from typing import Any

from page_objects.elements.UserLoginForm import UserLoginForm


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--url",
        default="test",
        help="URL start tests",
        choices=["test", "prod", "pp"]
    )
    group.addoption(
        "--browser",
        action="append",
        default=["firefox"],
        help="Browser engine which should be used",
        choices=["chromium", "firefox", "webkit"]
    )
    group.addoption(
        "--headed",
        default=True,
        help="Run tests in headed mode.",
        choices=['True', 'False']
    )
    group.addoption(
        "--browser-channel",
        action="store",
        default=None,
        help="Browser channel to be used."
    )
    group.addoption(
        "--slowmo",
        default=0,
        type=int,
        help="Run tests with slow mo"
    )
    group.addoption(
        "--output",
        default="test-results",
        help="Directory for artifacts produced by tests, defaults to test-results."
    )
    group.addoption(
        "--screenshot",
        default="off",
        choices=["on", "off", "only-on-failure"],
        help="Whether to automatically capture a screenshot after each test.",
    )
    group.addoption(
        "--full-page-screenshot",
        action="store_true",
        default=False,
        help="Whether to take a full page screenshot"
    )


@pytest.fixture(autouse=True, scope='session')
def driver(request):
    headed = request.config.getoption("--headed")
    url = request.config.getoption('--url')
    screenshot = request.config.getoption('--screenshot')

    webdriver = Driver(headed=headed, url=url, screenshot=screenshot)

    yield webdriver

    try:
        webdriver.quit()
    finally:
        webdriver.__class__._instances = {}
