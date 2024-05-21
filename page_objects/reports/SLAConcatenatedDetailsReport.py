from locator import Locator
from page import Page
import testit


class SLAConcatenatedDetailsReport(Page):
    name = 'Соединенный Детальный отчёт о результатах работы по SLA'
    path = 'report/sla_concatenated_details_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report():
        with testit.step(f'Проверить открытие отчета "{SLAConcatenatedDetailsReport.name}" по адресу "{SLAConcatenatedDetailsReport.path}"'):
            return Locator(SLAConcatenatedDetailsReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLAConcatenatedDetailsReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
