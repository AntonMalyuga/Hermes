import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class HermesAPI:
    login = os.getenv('HERMES_LOGIN')
    password = os.getenv('HERMES_PASSWORD')
    url = 'https://hermes-test.rt.ru/'

    @classmethod
    def _api(cls, data: dict, url: str) -> BeautifulSoup:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        url = f'{cls.url}{url}'
        res = requests.post(url=url, data=data, headers=headers, auth=(cls.login, cls.password))
        return BeautifulSoup(res.text, 'html.parser')

    @classmethod
    def rollback_order(cls, order_id: int):
        data = {
            'orders_list': order_id,
            "admin_types": 'orders_revert',
            "do": 1
        }
        res = cls._api(data=data, url='nsi/Orders/AdminOrders')
        quotes = res.find_all('p')
