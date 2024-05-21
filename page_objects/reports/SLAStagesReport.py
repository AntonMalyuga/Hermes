from locator import Locator
from page import Page
import testit


class SLAStagesReport(Page):
    name = 'Анализ просроченных клиентских заявок'
    path = 'report/sla_stages_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{SLAStagesReport.name}" по адресу "{SLAStagesReport.path}"'):
            return Locator(SLAStagesReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLAStagesReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
