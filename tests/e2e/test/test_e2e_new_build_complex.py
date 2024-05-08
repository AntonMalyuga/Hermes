import testit
from page_objects.forms.b2cCreationSMROrder import B2CCreateSMROrder
from page_objects.orders.b2c.SMR import SMR
from page_objects.orders.b2c.Project import Project
from page_objects.components.ComponentCreateProjectButton import ComponentCreateProjectButton
from page_objects.forms.b2cCreateConstructionProjectShow import B2CCreateConstructionProjectShow
from page_objects.orders.b2c.GPH import GPH
from page_objects.forms.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.forms.b2cFormSpecification import B2cFormSpecification
from page_objects.components.ComponentControlDate import ComponentControlDate
from page_objects.components.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.components.ComponenOrderstHierarchy import ComponentOrdersHierarchy
from page_objects.components.ComponentTypeProject import ComponentTypeProject
from page_objects.components.ComponentFiles import ComponentFiles


@testit.workItemIds(930)
@testit.title('E2E')
@testit.displayName('E2E по типу строительства "Комплексная новостройка"')
@testit.description('E2E по типу строительства "Комплексная новостройка" с услугой WiFi  по ГПХ до полного завершения проекта')
def test_e2e_new_build_complex(driver):
    smr = {
        'building_type': 'Комплексная новостройка',
        'floors': 9,
        'entrances': 4,
        'flats': 4,
        'dh_counter': 100,
        'commerce_plan': 10,
        'ap_year': 2019,
        'location_name': 'Москва',
        'client': '111111111',
        'obj_type': 'Многоквартирный дом'
    }

    project = {
        'project_name': 'Автопрогон'
    }

    works = {
        'works_core': {
            'Восстановление газонного покрытия': {
                'type': 'СМР',
                'qty': 12,
                'method': 'ГПХ'
            },
            'Восстановление покрытия из брусчатки': {
                'type': 'СМР',
                'qty': 10,
                'method': 'ГПХ'
            }
        }
    }

    specifications = {
        'specifications_core': {
            'Wi-Fi оборудование 1': {
                'method': 'ГПХ'
            }
        }
    }

    B2CCreateSMROrder(driver).open()
    B2CCreateSMROrder(driver).create_smr_order_form(smr)
    SMR(driver).open_order(B2CCreateSMROrder(driver).get_creation_order())
    SMR(driver).close_stage(pass_name='Положительно', next_stage='Подготовка заявок и включение в проект',
                            comment='Тестовый прогон')
    ComponentCreateProjectButton(driver).confirm()
    B2CCreateConstructionProjectShow(driver).create_project(project)
    Project(driver).close_not_current_tab()
    Project(driver).close_stage(pass_name='Проработка целесообразна',
                                next_stage='Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Project(driver).open_form_work()
    B2cFormWorkVolume(driver).add_works(works)
    B2cFormWorkVolume(driver).close()
    Project(driver).open_form_specification()
    B2cFormSpecification(driver).add_specification(specifications)
    B2cFormSpecification(driver).close()
    Project(driver).close_stage(pass_name='Положительно', next_stage='Проработка ТР и внесение стоимости работ')
    ComponentCapitalCosts(driver).add_cost('привет мир', 300)
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение срока строительства и согласований')
    ComponentControlDate(driver).change_all_control_dates(33)
    Project(driver).close_stage(pass_name='Положительно', next_stage='Формирование доходной части и согласование ТЭО')
    ComponentTypeProject(driver).change_type_project('ЛИП')
    Project(driver).close_stage(pass_name='Согласование проекта будет проходить вне Гермес',
                                next_stage='Согласование проекта вне Гермес и выделение инвестиций')
    ComponentFiles(driver).add_file(name='Подтверждение ВХР', type='Подтверждение ВХР', file_name='file.txt')
    Project(driver).close_stage(pass_name='Проект согласован вне Гермес. Инвестиции выделены',
                                next_stage='Ожидание реализации проекта', is_auto=True)
    GPH(driver).open_order(ComponentOrdersHierarchy(driver).get_gph_number())
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Разработка ПД и РД")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Согласование ПД и РД")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Выполнение СМР/внесение статусов работ")
    ComponentFiles(driver).add_file(name='Протокол измерений ВОК', type='Протокол измерений ВОК', file_name='file.txt')
    ComponentFiles(driver).add_file(name='Таблица терминации (xls)', type='Таблица терминации (xls)',
                                    file_name='file.txt')
    ComponentFiles(driver).add_file(name='Схема организации связи', type='Схема организации связи',
                                    file_name='file.txt')
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Приемка выполненных работ")
    ComponentFiles(driver).add_file(name='Ведомость ВО (pdf)', type='Ведомость ВО (pdf)', file_name='file.txt')
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Приёмка минимального комплекта ИД")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Внесение в СЛТУ/предварительная готовность")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Разработка ИД")
    ComponentFiles(driver).add_file(name='Исполнительная документация', type='Исполнительная документация',
                                    file_name='file.txt')
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Приёмка ИД")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Внесение данных в СЛТУ в статусе Готов")
    GPH(driver).close_stage(pass_name="Положительно", next_stage="Строительство завершено")
    Project(driver).open_order(ComponentOrdersHierarchy(driver).get_project_number())
    Project(driver).check_current_stage('Проект реализован')
    assert True
