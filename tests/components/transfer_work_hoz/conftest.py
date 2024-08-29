import pytest
from faker import Faker
from dataclasses import dataclass, field

Faker.seed()
fake = Faker('ru_RU')


@dataclass
class Order:
    id: int = 1627171


@pytest.fixture
def order() -> Order:
    return Order()
