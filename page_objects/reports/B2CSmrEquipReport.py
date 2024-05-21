from locator import Locator
from page import Page
import testit


class B2CSmrEquipReport(Page):
    name = 'Отчет по оборудованию'
    path = 'report/b2c_smr_equip_report'

    _is_open_report = '//button[contains(., "Показать на экране")]'
    _LOCATOR_H2_NAME_REPORT = '//h2'

    @staticmethod
    def is_open_report() -> bool:
        with testit.step(f'Проверить открытие отчета "{B2CSmrEquipReport.name}" по адресу "{B2CSmrEquipReport.path}"'):
            return Locator(B2CSmrEquipReport._is_open_report).is_on_page()

    @staticmethod
    def get_name_report() -> str:
        name = Locator(B2CSmrEquipReport._LOCATOR_H2_NAME_REPORT).text
        with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
            return name
