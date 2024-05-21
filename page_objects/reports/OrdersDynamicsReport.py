from locator import Locator
from page import Page
import testit


class OrdersDynamicsReport(Page):
    name = 'Отчёт по динамике заявок за период'
    path = 'report/orders_dynamics_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{OrdersDynamicsReport.name}" по адресу "{OrdersDynamicsReport.path}"'):
            return Locator(OrdersDynamicsReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(OrdersDynamicsReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
