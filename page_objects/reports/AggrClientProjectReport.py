from locator import Locator
from page import Page
import testit


class AggrClientProjectReport(Page):
    name = 'Агрегированная Аналитика проекта'
    path = 'report/aggr_client_project_report'

    _is_open_report = 'button[formaction="/report/aggr_client_project_report/html"]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @classmethod
    def open_page(cls):
        with testit.step(f'Открыть ссылку: {cls.path}'):
            Page.open_with_path(path=cls.path)

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{AggrClientProjectReport.name}" по адресу "{AggrClientProjectReport.path}"'):
            return Locator(AggrClientProjectReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(AggrClientProjectReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
