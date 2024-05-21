from locator import Locator
from page import Page
import testit


class MinicaseB2BServiceReport(Page):
    name = 'Отчёт по услугам мини-кейса B2B'
    path = 'report/minicase_b2b_service_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{MinicaseB2BServiceReport.name}" по адресу "{MinicaseB2BServiceReport.path}"'):
            return Locator(MinicaseB2BServiceReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(MinicaseB2BServiceReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
