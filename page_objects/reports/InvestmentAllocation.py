from locator import Locator
from page import Page
import testit


class InvestmentAllocation(Page):
    name = 'Отчёт о результатах работы по выделению инвестиций'
    path = 'report/investment_allocation'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{InvestmentAllocation.name}" по адресу "{InvestmentAllocation.path}"'):
            return Locator(InvestmentAllocation._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(InvestmentAllocation._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
