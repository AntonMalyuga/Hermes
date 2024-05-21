from locator import Locator
from page import Page
import testit


class InvestmentAllocationConcatenatedDetails(Page):
    name = 'Соединенный детальный отчёт о результатах работы по выделению инвестиций'
    path = 'report/investment_allocation_concatenated_details'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{InvestmentAllocationConcatenatedDetails.name}" по адресу "{InvestmentAllocationConcatenatedDetails.path}"'):
            return Locator(InvestmentAllocationConcatenatedDetails._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(InvestmentAllocationConcatenatedDetails._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
