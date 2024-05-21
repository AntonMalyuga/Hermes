from locator import Locator
from page import Page
import testit


class SLAContractorRatingReport(Page):
    name = 'Отчёт рейтинг Подрядчиков по SLA'
    path = 'report/sla_contractor_rating_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(
                f'Проверить открытие отчета "{SLAContractorRatingReport.name}" по адресу "{SLAContractorRatingReport.path}"'):
            return Locator(SLAContractorRatingReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(SLAContractorRatingReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
