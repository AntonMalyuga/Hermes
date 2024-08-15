from playwright.sync_api import sync_playwright


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        self._playwright = sync_playwright().start()
        self.request = kwargs

        if self.request.get("url") == 'prod':
            self.url = 'https://hermes-prod.rt.ru/'
        elif self.request.get("url") == 'pp':
            self.url = 'https://hermes-pp.rt.ru/'
        else:
            self.url = 'https://hermes-test.rt.ru/'

        self.browser = self._playwright.chromium.launch(
            headless=True if self.request.get("headed") == "True" else False,
        )

        parameters = self._playwright.devices["Desktop Chrome"]
        parameters["viewport"] = {"width": 1920, "height": 1080}
        parameters["ignore_https_errors"] = True if self.request.get("url") == "pp" else False

        self.page = self.browser.new_page(**parameters)

    def quit(self):
        self.browser.close()
        self._playwright.stop()

    def switch_to_tab(self, tab_index: int):
        self.page = self.browser.contexts[0].pages[tab_index]
