from locator import Locator
from page import Page
import testit


class DrnStagesReport(Page):
    name = 'Отчёт по этапам проекта по высвобождению недвижимости'
    path = 'report/drn_stages_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{DrnStagesReport.name}" по адресу "{DrnStagesReport.path}"'):
            return Locator(DrnStagesReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(DrnStagesReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
