from locator import Locator
from page import Page
import testit


class SLTUControlAggrReport(Page):
    name = 'Агрегированный Отчёт по контролю корректности данных в СЛТУ'
    path = 'report/sltucontrol_aggr_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLTUControlAggrReport.name}" по адресу "{SLTUControlAggrReport.path}"'):
            return Locator(SLTUControlAggrReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLTUControlAggrReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
