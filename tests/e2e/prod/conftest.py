import pytest
from faker import Faker
from dataclasses import dataclass, field
from page_objects.forms.FormB2CCreateConstructionProjectShow import Project, Address
from page_objects.forms.FormB2CSpecification import Specification
from page_objects.forms.FormB2CWorkVolume import Works, Work

Faker.seed()

fake = Faker('ru_RU')


@pytest.fixture()
def project() -> Project:
    return Project(
        rf='РФ Саратовский',
        is_need_broad='Нет',
        is_type_construct='Новостройка',
        customer_inn='1111111111',
        project_name='Автопрогон',
        dh=120,
        service_key='Wi-Fi'
    )


@pytest.fixture()
def address() -> Address:
    return Address(
        city='Ульяновск',
        street='Авиационная',
        house_name='д. 1',
    )


@pytest.fixture()
def specifications() -> Specification:
    return Specification(
        specifications_key='Шасси для пассивных мультиплексоров CWDM',
        specifications_core=None,
        natural_indicator='Точки доступа',
        construct_method='Подрядный способ'
    )


@pytest.fixture()
def works(specifications) -> Works:
    works_key = [
        Work(
            name='Монтаж оптического кросса (ШКОН, ШКОС) ёмкостью 48-96 портов включительно',
            qty=12,
            natural_indicator='Точки доступа',
            type='СМР',
            construct_method=specifications.construct_method
        ),
        Work(
            name='Компенсация логистических затрат на транспортировку оборудования, при строительстве объекта на удаленности от 101 км до 200 км включительно, от склада Заказчика.',
            qty=2,
            natural_indicator='Точки доступа',
            type='СМР',
            construct_method=specifications.construct_method
        ),
    ]

    return Works(works_key=works_key, works_core=None)
