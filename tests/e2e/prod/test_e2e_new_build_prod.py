import time

import pytest
import testit
from page_objects.forms.FormB2CCreateConstructionProjectShow import FormB2CCreateConstructionProjectShow
from page_objects.orders.b2c.Project import Project
from page_objects.forms.FormB2CWorkVolume import B2cFormWorkVolume
from page_objects.forms.FormB2CSpecification import B2cFormSpecification


@testit.workItemIds(925)
@testit.title('E2E')
@testit.displayName('E2E по типу строительства "Новостройка" на продуктивной среде')
@testit.description(
    'E2E по типу строительства "Новостройка" с услугой WiFi  по подрядному способу и с отправкой в архив')
@pytest.mark.slow
def test_e2e_new_build_prod(project, address, works, specifications):
    FormB2CCreateConstructionProjectShow.open_by_default()
    FormB2CCreateConstructionProjectShow.create_project(project=project, address=address)
    Project.ComponentCheckListWiFi.add_cost_wifi(value='capex')
    Project.ComponentCloseStage.close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')

    project = Project.get_order_id()

    Project.wait_reload_page()
    B2cFormWorkVolume.open_with_path(f'b2c/works_volumes/{str(project)}')

    B2cFormWorkVolume.set_construct_method('Подрядный')
    B2cFormWorkVolume.add_works(works)

    Project.wait_reload_page()
    B2cFormSpecification.open_with_path(f'b2c/specification/{str(project)}')
    B2cFormSpecification.add_specification(specifications)

    Project.open_order(project)
    Project.ComponentCloseStage.close_stage(pass_name='Положительно',
                                            next_stage='Проработка ТР и внесение стоимости работ')
    Project.ComponentCapitalCosts.add_cost('привет мир', 300)
    Project.ComponentNaturalIndicator.add_random()

    Project.ComponentCloseStage.close_stage(pass_name='Положительно',
                                            next_stage='Согласование состава оборудования услуг ключ в проекте')
    Project.ComponentCloseStage.close_stage(pass_name='Положительно',
                                            next_stage='Уточнение срока строительства и согласований')
    Project.ComponentControlDate.change_all_control_dates(30)
    Project.ComponentCloseStage.close_stage(pass_name='Требуются уточнения',
                                            next_stage='Проработка ТР и внесение стоимости работ',
                                            comment='Требуется отправка проекта в архив')
    Project.ComponentCloseStage.close_stage(pass_name='Уточнение в ТУ', next_stage='Уточнение лин. данных в ОТУ',
                                            comment='Требуется отправка проекта в архив')
    Project.ComponentCloseStage.close_stage(pass_name='На уточнение в КБ РФ', next_stage='Уточнение в ГРЗиУК',
                                            comment='Требуется отправка проекта в архив')
    Project.ComponentCloseStage.close_stage(pass_name='Отрицательно',
                                            next_stage='Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу',
                                            comment='Требуется отправка проекта в архив')
    Project.ComponentCloseStage.close_stage(pass_name='Отказ', next_stage='Отказ в реализации', reason='Задублировано',
                                            comment='Отправка заявки в архив')

    assert True
