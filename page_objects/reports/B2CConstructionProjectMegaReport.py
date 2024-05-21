from locator import Locator
from page import Page
import testit


class B2CConstructionProjectMegaReport(Page):
    name = 'Мега отчёт по строительным проектам B2C'
    path = 'report/b2c_construction_project_mega_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{B2CConstructionProjectMegaReport.name}" по адресу "{B2CConstructionProjectMegaReport.path}"'):
            return Locator(B2CConstructionProjectMegaReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(B2CConstructionProjectMegaReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
