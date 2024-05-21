from locator import Locator
from page import Page
import testit


class CommentsReport(Page):
    name = 'Отчёт по комментариям'
    path = 'report/comments_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{CommentsReport.name}" по адресу "{CommentsReport.path}"'):
            return Locator(CommentsReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(CommentsReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
