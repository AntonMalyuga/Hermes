from locator import Locator
from page import Page
import testit


class ComplexInstallationReport(Page):
    name = 'Отчёт по заявкам со Сложной инсталляцией'
    path = 'report/complex_installation_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{ComplexInstallationReport.name}" по адресу "{ComplexInstallationReport.path}"'):
            return Locator(ComplexInstallationReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(ComplexInstallationReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
