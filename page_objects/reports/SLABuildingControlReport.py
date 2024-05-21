from locator import Locator
from page import Page
import testit


class SLABuildingControlReport(Page):
    name = 'Контроль стройки'
    path = 'report/sla_building_control_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLABuildingControlReport.name}" по адресу "{SLABuildingControlReport.path}"'):
            return Locator(SLABuildingControlReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLABuildingControlReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
