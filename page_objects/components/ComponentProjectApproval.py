import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.orders.Order import BasePage
import testit


class ComponentProjectApproval(BasePage):
    name = 'Согласование проекта'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Инвестиционный проект")]/ancestor::div[2]'
    _LOCATOR_GROUP = (By.XPATH, _GROUP)

    _LOCATOR_TR_APPROVAL_OSTI_RF = (By.XPATH, f'{_GROUP}//tr[td[text()="Согласование в ОСТИ РФ"]/parent::tr[1]//form]')
    _LOCATOR_TR_APPROVAL_OSTI_KC = (By.XPATH, f'{_GROUP}//tr[td[text()="Согласование ОСТИ КЦ"]/parent::tr[1]//form]')
    _LOCATOR_TR_APPROVAL_PLAN_KC = (
    By.XPATH, f'{_GROUP}//tr[td[text()="Согласование планирования КЦ"]/parent::tr[1]//form]')

    def _move_to_group(self):
        with testit.step(f'Перейти к группе'):
            self.check_loader()
            self.move_to_element((By.XPATH, self._GROUP))

    def _approve(self, element: WebElement):
        element.find_element(By.XPATH, '//button[contains(text(), "Согласовать")]').click()

    def _decline(self, element: WebElement):
        element.find_element(By.XPATH, '//button[contains(text(), "Отклонить")]').click()

    def _check_confirm_approval(self, element: WebElement) -> bool:
        return element.find_element(By.XPATH, '//b[contains(text(), "Заявка поставлена в очередь")]').is_displayed()

    def _commented(self, element: WebElement, comment: str = ''):
        element.find_element(By.XPATH, '//textarea[@name="comment"]').send_keys(comment)

    def _completed_approval(self, element: WebElement, is_approve: bool = True, comment: str = ''):
        if comment:
            self._commented(element, comment)
        if is_approve:
            self._approve(element)
        else:
            self._decline(element)

        self._check_confirm_approval(element)

    def approval_osti_rf(self, is_approve: bool, comment: str = None):
        self.check_loader()
        self._move_to_group()
        element = self.find_element(self._LOCATOR_TR_APPROVAL_OSTI_RF)
        self._completed_approval(element=element, is_approve=is_approve,
                                 comment=comment)

    def approval_osti_kc(self, is_approve: bool, comment: str = None):
        self.check_loader()
        self._move_to_group()
        element = self.find_element(self._LOCATOR_TR_APPROVAL_OSTI_KC)
        self._completed_approval(element=element, is_approve=is_approve,
                                 comment=comment)

    def approval_plan_kc(self, is_approve: bool, comment: str = None):
        self.check_loader()
        self._move_to_group()
        element = self.find_element(self._LOCATOR_TR_APPROVAL_PLAN_KC)
        self._completed_approval(element=element, is_approve=is_approve,
                                 comment=comment)
