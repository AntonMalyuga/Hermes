import os
import sys
import requests
import exceptiongroup


class Sys:
    def __init__(self):
        self.login = os.getenv('HERMES_LOGIN')
        self.password = os.getenv('HERMES_PASSWORD')
        self.url = 'https://hermes-test.rt.ru:8103/smOrderOne.phtml'

    def _api(self, data: dict):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        res = requests.post(url=self.url, data=data, headers=headers, auth=(self.login, self.password))
        print(res.text)

    def delete_order(self, order_id: int):
        try:
            data = {
                'Order_ID': order_id,
                "delOrderFullOrder": 'Удалить конкретно',
                "isForce": 1
            }

            self._api(data=data)

        except Exception:
            print(f'Удаление заявки {order_id} невозможно')

