import pytest
from faker import Faker
from page_objects.forms.FormB2BSpecification import Specification, ConstructionMethod
from dataclasses import dataclass, field

Faker.seed()
fake = Faker('ru_RU')


class Specifications:
    specification: list[Specification] = [
        Specification(
            name='Источник бесперебойного питания Intelligent II 600RMLT',
            construction_method=ConstructionMethod.gph
        ),
        Specification(
            name='Аккумуляторная батарея 12ML120',
            construction_method=ConstructionMethod.hoz
        ),
        Specification(
            name='PoE инжектор',
            construction_method=ConstructionMethod.contractor
        )
    ]


@dataclass
class Order:
    id: int = 1602625
    specification: Specification = field(default_factory=lambda: fake.random_element(Specifications.specification))


@pytest.fixture
def order() -> Order:
    return Order()
