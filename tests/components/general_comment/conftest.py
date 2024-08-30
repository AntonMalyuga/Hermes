import pytest
from faker import Faker
from dataclasses import dataclass, field

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Order:
    id: int
    stage_name: str
    comment: str = fake.text(max_nb_chars=30)


@pytest.fixture()
def order() -> Order:
    return Order(id=1627530, stage_name='Привязка к СЗ и спецификация работ')


@pytest.fixture()
def order_with_max_comment() -> Order:
    return Order(id=1627530, stage_name='Привязка к СЗ и спецификация работ', comment=fake.text(max_nb_chars=2001))