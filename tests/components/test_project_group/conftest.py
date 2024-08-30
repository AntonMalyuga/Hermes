import pytest
from faker import Faker
from page_objects.orders.b2b.Project import Project
from page_objects.components.ComponentProjectGroup import ComponentProjectGroup, ProjectGroups, ProjectGroup
from dataclasses import dataclass, field

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Order:
    id: int
    stage_name: str
    group_name: ProjectGroup = field(default_factory=lambda: fake.random_element(ProjectGroups.get_groups()))


@pytest.fixture()
def order() -> Order:
    return Order(id=1627531, stage_name='Уточнение услуг ТЭО')
