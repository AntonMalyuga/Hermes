from page_objects.b2cCreationSMROrder import B2CCreateSMROrder
from page_objects.orders.b2c.SMR import SMR
from page_objects.orders.b2c.Project import Project
from page_objects.orders.b2c.ComponentCreateProjectButton import ComponentCreateProjectButton
from page_objects.b2cCreateConstructionProjectShow import B2CCreateConstructionProjectShow
from page_objects.orders.b2c.Hoz import Hoz
from page_objects.orders.b2c.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.orders.b2c.b2cFormSpecification import B2cFormSpecification
from page_objects.orders.b2c.ComponentLoaderDH import ComponentLoaderDH
from page_objects.orders.b2c.ComponentAddressParameters import ComponentAdressParameters
from page_objects.orders.b2c.ComponentControlDate import ComponentControlDate
from page_objects.orders.b2c.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.orders.b2c.ComponenOrderstHierarchy import ComponentOrdersHierarchy
from page_objects.orders.b2c.ComponentTypeProject import ComponentTypeProject
from page_objects.orders.b2c.ComponentFiles import ComponentFiles
from page_objects.elements.UserLoginForm import UserLoginForm
from api.sys import Sys


def test_e2e_private_sector(driver):
    smr = {
        'building_type': 'Коттеджный посёлок/частный сектор',
        'location_name': 'Калужская область',
        'area': 'Боровский район',
        'village': 'Рыжково Деревня',
        'area_name': 'Тест1',
        'commerce_plan': '4',
        'ap_year': '2019'
    }

    works = {
        'works_core': {
            'Восстановление газонного покрытия': {
                'type': 'СМР',
                'qty': 12,
                'method': 'Хоз.способ'
            },
            'Восстановление покрытия из брусчатки': {
                'type': 'СМР',
                'qty': 10,
                'method': 'Хоз.способ'
            }
        }
    }

    specifications = {
        'specifications_core': {
            'Wi-Fi оборудование 1': {
                'method': 'Хоз.способ'
            }
        }
    }

    UserLoginForm(driver).autorization_default()
    B2CCreateSMROrder(driver).open()
    B2CCreateSMROrder(driver).create_smr_order_form(smr)
    SMR(driver).open_order(B2CCreateSMROrder(driver).get_creation_order())
    SMR(driver).close_stage(pass_name='Положительно', next_stage='Планирование застройки территории частного сектора',
                            comment='Тестовый прогон')
    ComponentLoaderDH(driver).add_dh(
        link='https://yandex.ru/maps/?um=constructor%3Ad3ebc1e3d9867f5332fa30f4418892459de4b6fc1da211fda23de869fe708924&source=constructorLink',
        file_name='Загрузка_дх.xlsx')
    ComponentAdressParameters(driver).add_abonents(abonents=5)
    SMR(driver).close_stage(pass_name='Положительно', next_stage='Проверка адресов КБ')
    SMR(driver).close_stage(pass_name='Положительно',
                            next_stage='Подготовка заявок и включение в проект по сущ. застройке/частному сектору')
    ComponentCreateProjectButton(driver).confirm()
    B2CCreateConstructionProjectShow(driver).enter_project_name('Автопрогон')
    B2CCreateConstructionProjectShow(driver).enter_create_project()
    Project(driver).close_not_current_tab()
    Project(driver).close_stage(pass_name='Проработка целесообразна',
                                next_stage='Корректировка состава объектов проекта ЧС/Существующей застройки')
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
    Hoz(driver).open_order(ComponentOrdersHierarchy(driver).get_hoz_number())
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Разработка ПД и РД")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Согласование ПД и РД")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Выполнение СМР/внесение статусов работ")
    ComponentFiles(driver).add_file(name='Протокол измерений ВОК', type='Протокол измерений ВОК', file_name='file.txt')
    ComponentFiles(driver).add_file(name='Таблица терминации (xls)', type='Таблица терминации (xls)',
                                    file_name='file.txt')
    ComponentFiles(driver).add_file(name='Схема организации связи', type='Схема организации связи',
                                    file_name='file.txt')
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Приемка выполненных работ")
    ComponentFiles(driver).add_file(name='Ведомость ВО (pdf)', type='Ведомость ВО (pdf)', file_name='file.txt')
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Приёмка минимального комплекта ИД")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Внесение в СЛТУ/предварительная готовность")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Разработка ИД")
    ComponentFiles(driver).add_file(name='Исполнительная документация', type='Исполнительная документация',
                                    file_name='file.txt')
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Приёмка ИД")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Внесение данных в СЛТУ в статусе Готов")
    Hoz(driver).close_stage(pass_name="Положительно", next_stage="Строительство завершено")
    Project(driver).open_order(ComponentOrdersHierarchy(driver).get_project_number())
    Project(driver).check_current_stage('Проект реализован')
    assert True


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

    UserLoginForm(driver).autorization_default()
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
    B2CCreateConstructionProjectShow(driver).enter_project_name('Автопрогон')
    B2CCreateConstructionProjectShow(driver).enter_create_project()
    Project(driver).close_not_current_tab()
    Project(driver).close_stage(pass_name='Проработка целесообразна',
                                next_stage='Корректировка состава объектов проекта ЧС/Существующей застройки')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Sys().delete_order(Project(driver).get_order_id())
    assert True
