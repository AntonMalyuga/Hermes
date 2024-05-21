from locator import Locator
from page import Page
import testit


class NonSynchronizedPricesReport(Page):
    name = 'Отчёт по не синхронизированным расценкам'
    path = 'report/non_synchronized_prices_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{NonSynchronizedPricesReport.name}" по адресу "{NonSynchronizedPricesReport.path}"'):
            return Locator(NonSynchronizedPricesReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(NonSynchronizedPricesReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
