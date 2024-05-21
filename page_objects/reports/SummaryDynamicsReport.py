from locator import Locator
from page import Page
import testit


class SummaryDynamicsReport(Page):
    name = 'Сводный отчёт по динамике заявок за период'
    path = 'report/summary_dynamics_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SummaryDynamicsReport.name}" по адресу "{SummaryDynamicsReport.path}"'):
            return Locator(SummaryDynamicsReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SummaryDynamicsReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
