from locator import Locator
from page import Page
import testit


class SLTUControlDetReport(Page):
    name = 'Детальный Отчёт по контролю корректности данных в СЛТУ'
    path = 'report/sltucontrol_det_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLTUControlDetReport.name}" по адресу "{SLTUControlDetReport.path}"'):
            return Locator(SLTUControlDetReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLTUControlDetReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
