from locator import Locator
from page import Page
import testit


class ExclusiveAddressesReport(Page):
    name = 'Отчёт по эксклюзивным адресам'
    path = 'report/exclusive_addresses_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{ExclusiveAddressesReport.name}" по адресу "{ExclusiveAddressesReport.path}"'):
            return Locator(ExclusiveAddressesReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(ExclusiveAddressesReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
