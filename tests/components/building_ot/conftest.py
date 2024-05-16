import pytest
from dataclasses import dataclass, field, asdict
from faker import Faker

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Order:
    id: int = 1604329


@pytest.fixture()
def order():
    return Order
