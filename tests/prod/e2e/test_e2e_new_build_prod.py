import testit
from page_objects.forms.b2cCreateConstructionProjectShow import B2CCreateConstructionProjectShow
from page_objects.orders.b2c.Project import Project
from page_objects.forms.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.forms.b2cFormSpecification import B2cFormSpecification
from page_objects.components.ComponentControlDate import ComponentControlDate
from page_objects.components.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.components.ComponentCheckListWiFi import ComponentCheckListWiFi
from page_objects.components.ComponentNaturalIndicators import ComponentNaturalIndicator
from page_objects.components.ComponentCloseStage import ComponentCloseStage


@testit.workItemIds(925)
@testit.title('E2E')
@testit.displayName('E2E по типу строительства "Новостройка" на продуктивной среде')
@testit.description(
    'E2E по типу строительства "Новостройка" с услугой WiFi  по подрядному способу и с отправкой в архив')
def test_e2e_new_build_prod(driver):
    project = {
        'rf': 'РФ Ульяновский',
        'is_need_broad': 'Нет',
        'is_type_construct': 'Новостройка',
        'customer_inn': '1111111111',
        'project_name': 'Автопрогон',
        'address': {
            'city': 'Ульяновск',
            'street': 'Авиационная',
            'house_name': 'д. 1',
        },
        'dh': 120,
        'service_key': 'Wi-Fi'
    }
    works = {
        'works_keys': {
            'Восстановление поврежденного канала кабельной канализации': {
                'type': 'СМР',
                'qty': 12,
                'natural_indicator': 'Точки доступа'
            },
            'Монтаж оптического кросса (ШКОН, ШКОС) ёмкостью 48-96 портов включительно': {
                'type': 'СМР',
                'qty': 10,
                'natural_indicator': 'Точки доступа'
            }
        }
    }

    specifications = {
        'specifications_keys': {
            'Шасси для пассивных мультиплексоров CWDM': {
                'natural_indicator': 'Точки доступа'
            }
        },
        'constuct_method': 'Подрядный способ'
    }

    B2CCreateConstructionProjectShow(driver).open()
    B2CCreateConstructionProjectShow(driver).create_project(project)
    ComponentCheckListWiFi(driver).add_cost_wifi(value='capex')
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Project(driver).open_form_work()
    B2cFormWorkVolume(driver).set_construct_method('Подрядный')
    B2cFormWorkVolume(driver).add_works(works)
    B2cFormWorkVolume(driver).close()
    Project(driver).open_form_specification()
    B2cFormSpecification(driver).add_specification(specifications)
    B2cFormSpecification(driver).close()
    ComponentCloseStage(driver).close_stage(pass_name='Положительно',
                                            next_stage='Проработка ТР и внесение стоимости работ')
    ComponentCapitalCosts(driver).add_cost('привет мир', 300)
    ComponentNaturalIndicator(driver).add_random()
    ComponentCloseStage(driver).close_stage(pass_name='Положительно',
                                            next_stage='Согласование состава оборудования услуг ключ в проекте')
    ComponentCloseStage(driver).close_stage(pass_name='Положительно',
                                            next_stage='Уточнение срока строительства и согласований')
    ComponentControlDate(driver).change_all_control_dates(30)
    ComponentCloseStage(driver).close_stage(pass_name='Требуются уточнения',
                                            next_stage='Проработка ТР и внесение стоимости работ',
                                            comment='Требуется отправка проекта в архив')
    ComponentCloseStage(driver).close_stage(pass_name='Уточнение в ТУ', next_stage='Уточнение лин. данных в ОТУ',
                                            comment='Требуется отправка проекта в архив')
    ComponentCloseStage(driver).close_stage(pass_name='Уточнение в ТУ', next_stage='На уточнение в КБ РФ',
                                            comment='Требуется отправка проекта в архив')
    ComponentCloseStage(driver).close_stage(pass_name='Отрицательно',
                                            next_stage='Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу',
                                            comment='Требуется отправка проекта в архив')
    ComponentCloseStage(driver).close_stage(pass_name='Отказ', next_stage='Отказ в реализации',
                                            comment='Отправка заявки в архив')
    assert True
