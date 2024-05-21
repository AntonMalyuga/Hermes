from locator import Locator
from page import Page
import testit


class RerInventoryNumbers(Page):
    name = 'Отчет по инвентарным номерам'
    path = 'report/rer_inventory_numbers'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{RerInventoryNumbers.name}" по адресу "{RerInventoryNumbers.path}"'):
            return Locator(RerInventoryNumbers._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(RerInventoryNumbers._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
