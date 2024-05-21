from locator import Locator
from page import Page
import testit


class RerSubtask(Page):
    name = 'Детальный отчёт по подзадачам'
    path = 'report/rer_subtask'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{RerSubtask.name}" по адресу "{RerSubtask.path}"'):
            return Locator(RerSubtask._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(RerSubtask._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
