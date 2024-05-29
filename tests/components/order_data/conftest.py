import pytest
from dataclasses import dataclass, field, asdict
from faker import Faker

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Order:
    id: int = 1598428
    stage_name: str = 'Проработка ТР и внесение стоимости работ'


@pytest.fixture()
def order_id():
    return Order
