from locator import Locator
from page import Page
import testit


class SLADynamicReport(Page):
    name = 'Динамика показателей по SLA'
    path = 'report/sla_dynamic_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLADynamicReport.name}" по адресу "{SLADynamicReport.path}"'):
            return Locator(SLADynamicReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLADynamicReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
