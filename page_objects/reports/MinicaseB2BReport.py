from locator import Locator
from page import Page
import testit


class MinicaseB2BReport(Page):
    name = 'Отчёт по мини-кейсам B2B'
    path = 'report/minicase_b2b_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{MinicaseB2BReport.name}" по адресу "{MinicaseB2BReport.path}"'):
            return Locator(MinicaseB2BReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(MinicaseB2BReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
