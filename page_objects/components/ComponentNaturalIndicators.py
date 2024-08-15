import random
import testit
from page import Page
from locator import Locator, Input


class ComponentNaturalIndicator(Page):
    name = 'B2C: Натуральные показатели'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Натуральные показатели")]/ancestor::div[2]'
    _COMPONENT_BUTTON_OPEN_EDITOR = f'{_GROUP}//a[@title="Редактировать"]'
    _COMPONENT_BUTTON_SAVE = f'{_GROUP}//button[@type="submit"]'

    @classmethod
    def open_editor(cls):
        with testit.step(f'Открыть редактор'):
            Locator(cls._COMPONENT_BUTTON_OPEN_EDITOR).click()

    @classmethod
    def set_random_qty(cls):
        locator = f'{cls._GROUP}//input[@type="number"]'
        Locator(locator).is_on_page()
        inputs = Input(locator).all

        for input_element in inputs:
            input_element.press('Control+A')
            input_element.press('Backspace')
            input_element.fill(str(random.randint(1, 9)))

    @classmethod
    def save(cls):
        with testit.step(f'Сохранить'):
            Input(cls._COMPONENT_BUTTON_SAVE).click()

    @classmethod
    def add_random(cls):
        with testit.step(f'Добавить случайные'):
            cls.open_editor()
            cls.set_random_qty()
            cls.save()
