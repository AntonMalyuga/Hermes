import pytest
from faker import Faker
from api.Hermes import HermesAPI
from dataclasses import dataclass, field, asdict


Faker.seed()
fake = Faker('ru_RU')


@dataclass
class OrderOnStageDevelopmentTechnicalSolution:
    id: int = 1598807
    stage_name: str = 'Проработка ТР и внесение стоимости работ'


@dataclass
class OrderOnStageClarificationInGRZIUK:
    id: int = 1605479
    stage_name: str = 'Уточнение в ГРЗиУК'


@dataclass
class OrderOnStageCorrectObjectProjectAndPreTEO:
    id: int = 1605518
    child_id: int = 1605519
    comment: str = fake.text(max_nb_chars=10)
    reason: str = 'Задублировано'
    stage_name: str = 'Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу'


@dataclass
class OrderOnStageClarificationDeadline:
    id: int = 1605534
    child_id: int = 1605535
    comment: str = fake.text(max_nb_chars=10)
    stage_name: str = 'Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу'


@pytest.fixture()
def order_on_stage_development_technical_solution():
    return OrderOnStageDevelopmentTechnicalSolution


@pytest.fixture()
def order_on_stage_clarification_in_grziuk():
    return OrderOnStageClarificationInGRZIUK


@pytest.fixture()
def order_on_stage_correct_object_project_and_pre_teo():
    yield OrderOnStageCorrectObjectProjectAndPreTEO
    HermesAPI().rollback_order(OrderOnStageCorrectObjectProjectAndPreTEO.id)
    HermesAPI().rollback_order(OrderOnStageCorrectObjectProjectAndPreTEO.child_id)


@pytest.fixture()
def order_on_stage_clarification_deadline():
    yield OrderOnStageClarificationDeadline
    HermesAPI().rollback_order(OrderOnStageClarificationDeadline.id)
    HermesAPI().rollback_order(OrderOnStageClarificationDeadline.child_id)

