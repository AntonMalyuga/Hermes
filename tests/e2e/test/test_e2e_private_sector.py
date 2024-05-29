from page_objects.forms.FormB2CCreationSMROrder import FormB2CCreationSMROrder
from page_objects.orders.b2c.SMR import SMR
from page_objects.orders.b2c.Project import Project
from page_objects.components.ComponentCreateProjectButton import ComponentCreateProjectButton
from page_objects.forms.FormB2CCreateConstructionProjectShow import FormB2CCreateConstructionProjectShow
from page_objects.components.ComponentLoaderDH import ComponentLoaderDH
from page_objects.components.ComponentAddressParameters import ComponentAdressParameters
from api.Sys import Sys
import testit
import pytest


@testit.workItemIds(929)
@testit.title('E2E')
@testit.displayName('E2E по типу строительства "Частный сектор"')
@testit.description('E2E по типу строительства "Частный сектор"  с услугой CORE до удаления созданной заявки проекта и заявки СМР')
@pytest.mark.slow
def test_e2e_private_sector_and_delete(driver):
    smr = {
        'building_type': 'Коттеджный посёлок/частный сектор',
        'location_name': 'Калужская область',
        'area': 'Боровский район',
        'village': 'Рыжково Деревня',
        'area_name': 'Тест1',
        'commerce_plan': '4',
        'ap_year': '2019'
    }

    project = {
        'project_name': 'Автопрогон'
    }

    B2CCreateSMROrder(driver).open()
    B2CCreateSMROrder(driver).create_smr_order_form(smr)
    SMR(driver).open_order(B2CCreateSMROrder(driver).get_creation_order())
    SMR(driver).close_stage(pass_name='Положительно',
                            next_stage='Планирование застройки территории частного сектора',
                            comment='Тестовый прогон')
    ComponentLoaderDH(driver).add_dh(
        link='https://yandex.ru/maps/?um=constructor%3Ad3ebc1e3d9867f5332fa30f4418892459de4b6fc1da211fda23de869fe708924&source=constructorLink',
        file_name='Загрузка_дх.xlsx')
    ComponentAdressParameters(driver).add_abonents(abonents=5)
    SMR(driver).close_stage(pass_name='Положительно', next_stage='Проверка адресов КБ')
    SMR(driver).close_stage(pass_name='Положительно',
                            next_stage='Подготовка заявок и включение в проект по сущ. застройке/частному сектору')
    ComponentCreateProjectButton(driver).confirm()
    B2CCreateConstructionProjectShow(driver).create_project(project=project, is_prepared=True)
    Project(driver).close_not_current_tab()
    Project(driver).close_stage(pass_name='Проработка целесообразна',
                                next_stage='Корректировка состава объектов проекта ЧС/Существующей застройки')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Sys().delete_order(Project(driver).get_order_id())
    assert True
