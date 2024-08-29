from page import Page
from abc import ABC, abstractmethod, ABCMeta
from locator import Locator, Input, Select, CheckBox
import testit


class ComponentInterface:
    name: str
    group_name: str

    def __call__(self, *args, **kwargs):
        self.locators = []
        for locator in args:
            self.locators.append(f'{self.__get_group_xpath()}//{locator}')

    def __get_group_xpath(self):
        return f'//div[@class="panel panel-material"]//span[contains(., "{self.group_name}")]/ancestor::div[2]'
