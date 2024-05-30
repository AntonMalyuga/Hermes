import pytest
from faker import Faker
from VO.FormB2BCreateOldProject import Project

Faker.seed()
fake = Faker('ru_RU')


@pytest.fixture()
def project() -> Project:
    return Project(
        client_name='АВТОТЕСТ',
        client_inn='000000000001',
        client_kpp='100000001',
        contact_name='Малюга А.С.',
        contact_telephone_number='8(999)999-99-99',
        contact_email='test@test.test',
        new_project_name='Проект проект уникальщина',
        manager_kb_name='Малюга А.С.',
        manager_kb_telephone_number='8(999)999-99-99',
        manager_kb_email='testkb@test.test',
        manager_kb_macro_segment='B2B',
        manager_kb_segment='Клиенты федерального уровня (ККФУ)',
        chanel_sales='Активный канал/3К АП (хантеры)',
        organization_term=fake.future_date().strftime('%d.%m.%Y'),
        location_lvl_one='Саратовская Область',
        location_lvl_two='Саратов Город',
        street='ул Авиастроителей',
        house='д. 3',
        srv_fee_install=fake.random_int(min=1000, max=20000, step=1000),
        service_qty=fake.random_int(min=1, max=10, step=1),
        fee_monthly=fake.random_int(min=100, max=2000, step=100),
        scale_servie_speed='кбит/с',
        service_speed=fake.random_int(min=10, max=200, step=10)
    )


@pytest.fixture()
def project_on_teo(project):
    project.is_teo = True
    return project


@pytest.fixture()
def project_on_teo_and_tvp(project):
    project.is_teo = True
    project.is_tvp = True
    return project


@pytest.fixture()
def project_on_pre_teo(project):
    project.is_teo = False
    return project


@pytest.fixture()
def project_on_pre_teo_and_tvp(project):
    project.is_teo = False
    project.is_tvp = True
    return project
