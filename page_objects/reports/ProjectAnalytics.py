from locator import Locator
from page import Page
import testit


class ProjectAnalytics(Page):
    name = 'Аналитика проекта'
    path = 'report/projectanalytics'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{ProjectAnalytics.name}" по адресу "{ProjectAnalytics.path}"'):
            return Locator(ProjectAnalytics._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(ProjectAnalytics._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
