from locator import Locator
from page import Page
import testit


class SLTUConstructionControlReport(Page):
    name = 'Отчёт по контролю занесения данных в СЛТУ'
    path = 'report/sltu_construction_control_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLTUConstructionControlReport.name}" по адресу "{SLTUConstructionControlReport.path}"'):
            return Locator(SLTUConstructionControlReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLTUConstructionControlReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
