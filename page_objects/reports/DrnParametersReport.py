from locator import Locator
from page import Page
import testit


class DrnParametersReport(Page):
    name = 'Отчёт по параметрам проекта по высвобождению недвижимости формируемый'
    path = 'report/drn_parameters_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{DrnParametersReport.name}" по адресу "{DrnParametersReport.path}"'):
            return Locator(DrnParametersReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(DrnParametersReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
