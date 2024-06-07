import pytest
from faker import Faker
from VO.Attachents import AttachmentTypes
from dataclasses import dataclass, field

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Attachment:
    file_name_in_path: str = 'test_file.txt'
    file_alternative_name: str = field(default_factory=lambda: fake.text(max_nb_chars=20))
    attachment_type: AttachmentTypes = field(default_factory=lambda: fake.random_element(AttachmentTypes.types))


@dataclass
class Order:
    id: int = 1605794
    stage_name: str = 'Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу'


@pytest.fixture()
def order():
    return Order


@pytest.fixture()
def attachment():
    return Attachment()


@pytest.fixture()
def attachment_list() -> list[Attachment]:
    return [Attachment(), Attachment(), Attachment()]

