import pytest
from faker import Faker
from page_objects.forms.FormB2BWorkVolume import Work
from dataclasses import dataclass, field

Faker.seed()
fake = Faker('ru_RU')


class WorksList:
    works: list[Work] = [
        Work(name='Восстановление газонного покрытия', work_type='СМР', count=fake.random_int(1, 15)),
        Work(name='Восстановление газонного покрытия', work_type='ПИР', count=fake.random_int(1, 15)),
        Work(name='Выполнение работ по программированию ключа', work_type='СМР', count=fake.random_int(1, 15)),
        Work(name='Демонтаж АРМ/периферийного устройства', work_type='СМР', count=fake.random_int(1, 15)),
        Work(name='Демонтаж и отключение розетки', work_type='СМР', count=fake.random_int(1, 15)),
        Work(name='Демонтаж кабель каналов, коробов ПВХ (без материалов)', work_type='СМР', count=fake.random_int(1, 15))
    ]


@dataclass
class Order:
    id: int = 1602625
    work: Work = field(default_factory=lambda: fake.random_element(WorksList.works))

@dataclass
class OrderWithCluster:
    id: int = 1597444

@pytest.fixture
def order() -> Order:
    return Order()

@pytest.fixture
def order_with_cluster() -> OrderWithCluster:
    return OrderWithCluster()