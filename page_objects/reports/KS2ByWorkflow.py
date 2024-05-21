from locator import Locator
from page import Page
import testit


class KS2ByWorkflow(Page):
    name = 'Отчёт по КС-2'
    path = 'report/ks2_by_workflow'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{KS2ByWorkflow.name}" по адресу "{KS2ByWorkflow.path}"'):
            return Locator(KS2ByWorkflow._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(KS2ByWorkflow._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
