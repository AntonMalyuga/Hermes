import testit
from locator import Locator


class Alert:
    name = 'Предупреждение'

    _ALERT = '#toast-container span'
    _ALERT_404_STATUS = '#toast-container .toast-message'

    @staticmethod
    def check_alert():
        if len(Locator(Alert._ALERT).get_all_elements()) == 0:
            return True
        else:
            raise f'Получена ошибка в приложении: {Alert.get_alert_text()}'

    @staticmethod
    def get_alert_text() -> str:
        alert_text = str(Locator(Alert._ALERT).text)
        with testit.step(f'Получить текст предупреждения "{alert_text}"'):
            return alert_text

    @staticmethod
    def get_alert_resource_not_found(self):
        alert_text = str(Locator(Alert._ALERT_404_STATUS).text)
        with testit.step(f'Получить предупреждение об ошибке если ресурс не найден "{alert_text}"'):
            return alert_text
