import time
from page import Page
from locator import Locator, Input, Select
import testit


class ComponentProjectApproval(Page):
    name = 'B2B: Согласование проекта'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]'
    _LOCATOR_TR_APPROVAL_OSTI_RF = f'{_GROUP}//tr[td[text()="Согласование в ОСТИ РФ"]/parent::tr[1]//form]'
    _LOCATOR_TR_APPROVAL_OSTI_KC = f'{_GROUP}//tr[td[text()="Согласование ОСТИ КЦ"]/parent::tr[1]//form]'
    _LOCATOR_TR_APPROVAL_PLAN_KC = f'{_GROUP}//tr[td[text()="Согласование планирования КЦ"]/parent::tr[1]//form]'

    @classmethod
    def _approve(cls, element: Locator):
        element.locator('//button[contains(text(), "Согласовать")]').click()

    @classmethod
    def _decline(cls, element: Locator):
        element.locator('//button[contains(text(), "Отклонить")]').click()

    @classmethod
    def _check_confirm_approval(cls, element: Locator) -> bool:
        return element.locator('//b[contains(text(), "Заявка поставлена в очередь")]').is_disabled()

    @classmethod
    def _commented(cls, element: Locator, comment: str = ''):
        element.locator('//textarea[@name="comment"]').fill(comment)

    @classmethod
    def _completed_approval(cls, element: Locator, is_approve: bool = True, comment: str = ''):
        if comment:
            cls._commented(element, comment)
        if is_approve:
            cls._approve(element)
        else:
            cls._decline(element)

        cls._check_confirm_approval(element)

    @classmethod
    def approval_osti_rf(cls, is_approve: bool, comment: str = None):
        element = Locator(cls._LOCATOR_TR_APPROVAL_OSTI_RF)
        cls._completed_approval(element=element, is_approve=is_approve,
                                comment=comment)

    @classmethod
    def approval_osti_kc(cls, is_approve: bool, comment: str = None):
        element = Locator(cls._LOCATOR_TR_APPROVAL_OSTI_KC)
        cls._completed_approval(element=element, is_approve=is_approve,
                                comment=comment)

    @classmethod
    def approval_plan_kc(cls, is_approve: bool, comment: str = None):
        element = Locator(cls._LOCATOR_TR_APPROVAL_PLAN_KC)
        cls._completed_approval(element=element, is_approve=is_approve,
                                comment=comment)
