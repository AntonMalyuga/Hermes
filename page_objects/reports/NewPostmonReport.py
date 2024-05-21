from locator import Locator
from page import Page
import testit


class NewPostmonReport(Page):
    name = 'Отчёт по фактическим доходам для Постмониторинга'
    path = 'report/new_postmon_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{NewPostmonReport.name}" по адресу "{NewPostmonReport.path}"'):
            return Locator(NewPostmonReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(NewPostmonReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
