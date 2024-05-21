from locator import Locator
from page import Page
import testit


class LocalClientOrderReport(Page):
    name = 'Отчёт по клиентским заявкам (формируемый)'
    path = 'report/local_client_order_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{LocalClientOrderReport.name}" по адресу "{LocalClientOrderReport.path}"'):
            return Locator(LocalClientOrderReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(LocalClientOrderReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
