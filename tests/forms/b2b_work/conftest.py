import pytest
from faker import Faker
from dataclasses import dataclass, field

Faker.seed()
fake = Faker('ru_RU')


@dataclass
class Work:
    name: str
    work_type: str
    count: int = fake.random_int(0, 15)


class WorksList:
    works: list[Work] = [
        Work(name='Восстановление газонного покрытия', work_type='СМР'),
        Work(name='Восстановление газонного покрытия', work_type='ПИР'),
        Work(name='Выполнение работ по программированию ключа', work_type='СМР'),
        Work(name='Демонтаж АРМ/периферийного устройства', work_type='СМР'),
        Work(name='Демонтаж и отключение розетки', work_type='СМР'),
        Work(name='Демонтаж кабель каналов, коробов ПВХ', work_type='СМР')
    ]


@dataclass
class Order:
    id: int = 1602625
    works: Work = field(default_factory=lambda: fake.random_element(WorksList.works))


@pytest.fixture
def order() -> Order:
    return Order()
