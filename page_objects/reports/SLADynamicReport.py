import testit
from driver import Driver


class SLADynamicReport:
    name = 'Динамика показателей по SLA'
    path = 'report/sla_dynamic_report'

    @staticmethod
    def check_report():
        Driver().get_by_role('button', 'Показать на экране').click()

    #
    # _LOCATOR_H2_NAME_REPORT = (By.XPATH, '//h2')

    # @classmethod
    # def check_report(cls):
    #     with testit.step(f'Проверить открытие отчета "{cls.name}" по адресу "{cls.path}"'):
    #         if len(cls.find_elements(cls._CHECK_REPORT)) > 0:
    #             return True
    #
    # @classmethod
    # def get_name_report(cls) -> str:
    #     name = cls.find_element(cls._LOCATOR_H2_NAME_REPORT).text
    #     with testit.step(f'Получить имя отчёта в интерфейсе: {name}'):
    #         return name
