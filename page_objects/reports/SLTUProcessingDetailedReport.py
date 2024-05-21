from locator import Locator
from page import Page
import testit


class SLTUProcessingDetailedReport(Page):
    name = 'Отчёт по сквозному прохождению заявок на организацию (детальный)'
    path = 'report/sltu_processing_detailed_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLTUProcessingDetailedReport.name}" по адресу "{SLTUProcessingDetailedReport.path}"'):
            return Locator(SLTUProcessingDetailedReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLTUProcessingDetailedReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
