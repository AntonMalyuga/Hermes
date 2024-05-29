import testit

from page_objects.components.VO.RowHistoryOrder import RowHistoryOrder
from locator import Locator
from page import Page


class ComponentHistoryStages(Page):
    name = 'История прохождения заявки'

    _LOCATOR_FORM_CLOSE_STAGE_PASS = '//table[contains(@class, "js--datatable-stage-history")]'

    @classmethod
    def __get_locator_row(cls, xpath_position: str) -> str:
        return f'{cls._LOCATOR_FORM_CLOSE_STAGE_PASS}//tbody//tr[{xpath_position}]'

    @classmethod
    def __get_stage_start(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[1]').text

    @classmethod
    def __get_stage_end(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[2]').text

    @classmethod
    def __get_stage_name(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[3]').text

    @classmethod
    def __get_result(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[4]').text

    @classmethod
    def __get_user_name(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[5]').text

    @classmethod
    def __get_reason(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[6]').text.strip()

    @classmethod
    def __get_comment(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[7]').text

    @classmethod
    def __get_appointed(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[8]').text

    @classmethod
    def __get_appointed_date(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[9]').text

    @classmethod
    def __get_roles(cls, xpath_position: str) -> str:
        return Locator(f'{cls.__get_locator_row(xpath_position)}//td[10]').text

    @classmethod
    def get_data_close_stage_by_row(cls, xpath_position: str) -> RowHistoryOrder:
        with testit.step(f'Получить данные истории по локатору {xpath_position}'):
            return RowHistoryOrder(
                stage_start=cls.__get_stage_start(xpath_position),
                stage_ent=cls.__get_stage_end(xpath_position),
                stage_name=cls.__get_stage_name(xpath_position),
                detail=None,
                result=cls.__get_result(xpath_position),
                user_name=cls.__get_user_name(xpath_position),
                reason=cls.__get_reason(xpath_position),
                comment=cls.__get_comment(xpath_position),
                appointed=cls.__get_appointed(xpath_position),
                appointed_date=cls.__get_appointed_date(xpath_position)
            )

    @classmethod
    def get_last_data_close_stage(cls) -> RowHistoryOrder:
        with testit.step('Получить данные последнего закрытого этапа'):
            return cls.get_data_close_stage_by_row('last()-1')

    @classmethod
    def get_first_data_close_stage(cls) -> RowHistoryOrder:
        with testit.step('Получить данные первого закрытого этапа'):
            return cls.get_data_close_stage_by_row('1')

    @classmethod
    def get_data_open_stage(cls) -> RowHistoryOrder:
        with testit.step('Получить данные открытого этапа'):
            return cls.get_data_close_stage_by_row('last()')
