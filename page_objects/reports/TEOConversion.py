from locator import Locator
from page import Page
import testit


class TEOConversion(Page):
    name = 'Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости'
    path = 'report/teo_conversion'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{TEOConversion.name}" по адресу "{TEOConversion.path}"'):
            return Locator(TEOConversion._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(TEOConversion._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
