from locator import Locator
from page import Page
import testit


class B2CPlanFactCharts(Page):
    name = 'Графические отчёты План/Факт'
    path = 'report/b2c_plan_fact_charts'

    _is_open_report = '//button[contains(., "В формат xlsx")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report():
        with testit.step(f'Проверить открытие отчета "{B2CPlanFactCharts.name}" по адресу "{B2CPlanFactCharts.path}"'):
            return Locator(B2CPlanFactCharts._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(B2CPlanFactCharts._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
