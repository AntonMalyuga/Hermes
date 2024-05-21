from locator import Locator
from page import Page
import testit


class SLAReportByStages(Page):
    name = 'Отчёт о результатах работы по SLA по этапам'
    path = 'report/sla_report_by_stages'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{SLAReportByStages.name}" по адресу "{SLAReportByStages.path}"'):
            return Locator(SLAReportByStages._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLAReportByStages._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
