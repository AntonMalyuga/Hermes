from dataclasses import dataclass

import pytest
from faker import Faker
from api.Sys import SysAPI
from page_objects.orders.b2b.Construction import Construction



Faker.seed()
fake = Faker('ru_RU')


@dataclass
class Order:
    id: int


@pytest.fixture
def order() -> Order:
    order = Order(1627523)
    return order


@pytest.fixture
def order_with_delete() -> Order:
    order = Order(1627529)
    yield order
    Construction.open_order(order.id)
    SysAPI.delete_order(Construction.ComponentB2BOrdersHierarchy.get_gph_number())
