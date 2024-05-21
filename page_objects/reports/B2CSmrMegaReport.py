from locator import Locator
from page import Page
import testit


class B2CSmrMegaReport(Page):
    name = 'Мега отчёт по объектам B2C'
    path = 'report/b2c_smr_mega_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{B2CSmrMegaReport.name}" по адресу "{B2CSmrMegaReport.path}"'):
            return Locator(B2CSmrMegaReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(B2CSmrMegaReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
