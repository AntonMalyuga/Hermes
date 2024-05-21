from locator import Locator
from page import Page
import testit


class TEOConversionWithAptv(Page):
    name = 'Отчёт по конвертации ТЭО-Стройка с учетом срока окупаемости и с аналитикой АПТВ'
    path = 'report/teo_conversion_with_aptv'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{TEOConversionWithAptv.name}" по адресу "{TEOConversionWithAptv.path}"'):
            return Locator(TEOConversionWithAptv._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(TEOConversionWithAptv._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
