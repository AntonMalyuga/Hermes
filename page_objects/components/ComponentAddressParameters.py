from selenium.webdriver.common.by import By
from page_objects.orders.Order import Order
import testit


class ComponentAdressParameters(Order):
    _LOCATOR_GROUP = (
        By.XPATH,
        '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]')
    _LOCATOR_EDIT_FORM = (By.XPATH,
                          '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//i[@class = "glyphicon-edit glyphicon"]')

    _LOCATOR_ABONENT_COUNT = (By.XPATH,
                              '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "active_subscribers_count"]')
    _LOCATOR_SET_ABONENTS_BUTTON = (By.XPATH,
                                    '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//form[@class = "form js--load-element"]//button[@type= "submit"]')
    _LOCATOR_YANDEX_LINK = (By.XPATH,
                            '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@name= "yandex_constructor_link"]')
    _LOCATOR_SET_FILE_BUTTON = (By.XPATH,
                                '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//input[@class= "form-control input-sm js--extract-file-name-on-change"]')
    _LOCATOR_LOAD_FILE_BUTTON = (By.XPATH,
                                 '//div[@class="panel panel-material"]//span[contains(., "Параметры объекта на адресе")]/ancestor::div[2]//div[@class = "form-group"]//button[@type= "submit"]')

    def __push_edit_form(self):
        with testit.step(f'Открыть редактирование параметров адреса', 'Форма редактирования открыта'):
            self.find_element(locator=self._LOCATOR_EDIT_FORM).click()

    def __set_abonents(self, abonents):
        with testit.step(f'Set abonent {abonents}'):
            self.find_element(locator=self._LOCATOR_ABONENT_COUNT).clear()
            self.find_element(locator=self._LOCATOR_ABONENT_COUNT).send_keys(abonents)

    def __push_set_abonents_button(self):
        with testit.step(f'Нажать кнопку сохранения параметров адреса', 'Сохранение успешно'):
            self.find_element(locator=self._LOCATOR_SET_ABONENTS_BUTTON).click()

    def move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.move_to_element(self._LOCATOR_GROUP)

    @testit.step('Add abbonents')
    def add_abonents(self, abonents: int):
        with testit.step(f'Добавить абонентов "{abonents}"'):
            self.check_loader()
            self.move_to_group()
            self.__push_edit_form()
            self.__set_abonents(abonents)
            self.__push_set_abonents_button()
