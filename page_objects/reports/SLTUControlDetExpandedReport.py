from locator import Locator
from page import Page
import testit


class SLTUControlDetExpandedReport(Page):
    name = 'Детальный Отчёт по контролю корректности данных в СЛТУ (расширенный)'
    path = 'report/sltucontrol_det_expanded_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLTUControlDetExpandedReport.name}" по адресу "{SLTUControlDetExpandedReport.path}"'):
            return Locator(SLTUControlDetExpandedReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLTUControlDetExpandedReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
