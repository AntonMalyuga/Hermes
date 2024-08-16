import testit
from page import Page
from locator import Locator, Select, Input


class Alert(Page):
    name = 'Предупреждение'

    _ALERT = '#toast-container span'
    _ALERT_404_STATUS = '#toast-container .toast-message'

    @classmethod
    def check_alert(cls):
        if len(Locator(cls._ALERT).text) == 0:
            return True
        else:
            raise f'Получена ошибка в приложении: {cls.get_alert_text()}'

    @classmethod
    def get_alert_text(cls) -> str:
        alert_text = str(Locator(cls._ALERT).text)
        with testit.step(f'Получить текст предупреждения "{alert_text}"'):
            return alert_text

    @classmethod
    def get_alert_resource_not_found(cls):
        alert_text = str(Locator(cls._ALERT_404_STATUS).text)
        with testit.step(f'Получить предупреждение об ошибке если ресурс не найден "{alert_text}"'):
            return alert_text
