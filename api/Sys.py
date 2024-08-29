import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SysAPI:
    login = os.getenv('HERMES_TEST_LOGIN')
    password = os.getenv('HERMES_TEST_PASSWORD')
    url = 'https://hermes-test.rt.ru:8103/smOrderOne.phtml'

    @classmethod
    def _api(cls, data: dict):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }


        response = requests.post(url=cls.url, data=data, headers=headers, auth=(cls.login, cls.password))
        print(response.text)

    @classmethod
    def delete_order(cls, order_id: int):
        data = {
            'Order_ID': order_id,
            "delOrderFullOrder": 'Удалить конкретно',
            "isForce": 1
        }

        cls._api(data=data)


if __name__ == '__main__':
    SysAPI.delete_order(123)