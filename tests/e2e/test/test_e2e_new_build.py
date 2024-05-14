import testit
import pytest
from page_objects.forms.FormB2CCreateConstructionProjectShow import FormB2CCreateConstructionProjectShow
from page_objects.orders.b2c.Project import Project
from page_objects.orders.b2c.Customer import Customer
from page_objects.orders.b2c.CustomerOrder import CustomerOrder
from page_objects.forms.FormB2CWorkVolume import B2cFormWorkVolume
from page_objects.forms.FormB2CSpecification import B2cFormSpecification
from page_objects.components.ComponentControlDate import ComponentControlDate
from page_objects.components.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.components.ComponentCheckListWiFi import ComponentCheckListWiFi
from page_objects.components.ComponentNaturalIndicators import ComponentNaturalIndicator
from page_objects.components.ComponentAddictionalIncome import ComponentAdditionalIncome
from page_objects.components.ComponenB2COrderstHierarchy import ComponentB2COrdersHierarchy
from page_objects.components.ComponentTypeProject import ComponentTypeProject
from page_objects.components.ComponentNumberDSOFU import ComponentNumberDSOFU
from page_objects.components.ComponentFiles import ComponentFiles
from page_objects.forms.FormB2CObjectOrder import FormB2CObjectOrder


@testit.workItemIds(925)
@testit.title('E2E')
@testit.displayName('E2E по типу строительства "Новостройка"')
@testit.description('E2E по типу строительства "Новостройка" с услугой WiFi  по подрядному способу без УЗ до полного завершения проекта')
@pytest.mark.slow
@pytest.mark.skip('HE-13781')
def test_e2e_new_build(driver):
    project = {
        'rf': 'РФ Саратовский',
        'is_need_broad': 'Нет',
        'is_type_construct': 'Новостройка',
        'customer_inn': '111111111111',
        'project_name': 'Автопрогон',
        'address': {
            'city': 'Саратов',
            'street': 'Авиастроителей',
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
            'Восстановление газонного покрытия': {
                'type': 'СМР',
                'qty': 10,
                'natural_indicator': 'Точки доступа'
            }
        }
    }

    specifications = {
        'specifications_keys': {
            'Wi-Fi оборудование 1': {
                'natural_indicator': 'Точки доступа'
            }
        },
        'constuct_method': 'Подрядный способ'
    }

    FormB2CCreateConstructionProjectShow(driver).open()
    FormB2CCreateConstructionProjectShow(driver).create_project(project)
    Project(driver).check_current_stage(
        'Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу')
    ComponentCheckListWiFi(driver).add_cost_wifi(value='capex')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Project(driver).open_form_work()
    B2cFormWorkVolume(driver).set_construct_method('Подрядный')
    B2cFormWorkVolume(driver).add_works(works)
    B2cFormWorkVolume(driver).close()
    Project(driver).open_form_specification()
    B2cFormSpecification(driver).add_specification(specifications)
    B2cFormSpecification(driver).close()
    Project(driver).close_stage(pass_name='Положительно', next_stage='Проработка ТР и внесение стоимости работ')
    ComponentCapitalCosts(driver).add_cost('привет мир', 300)
    ComponentNaturalIndicator(driver).add_random()
    Project(driver).close_stage(pass_name='Положительно',
                                next_stage='Согласование состава оборудования услуг ключ в проекте')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение срока строительства и согласований')
    ComponentControlDate(driver).change_all_control_dates(30)
    Project(driver).close_stage(pass_name='Положительно', next_stage='Формирование КП и калькулятора')
    ComponentFiles(driver).add_file(name='КП Ключ', type='КП Ключ', file_name='file.txt')
    ComponentFiles(driver).add_file(name='Калькулятор Ключ', type='Калькулятор Ключ', file_name='file.txt')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Формирование доходной части и согласование ТЭО')
    ComponentAdditionalIncome(driver).add_addictional_income(name='Вайфай', infrastructure_type='Wi-Fi',
                                                             income_type='WiFi', abonent_type='Приростная', value=10000)
    ComponentTypeProject(driver).change_type_project('ЛИП')
    Project(driver).close_stage(pass_name='Согласование проекта будет проходить вне Гермес',
                                next_stage='Согласование проекта вне Гермес и выделение инвестиций')
    ComponentFiles(driver).add_file(name='Подтверждение ВХР', type='Подтверждение ВХР', file_name='file.txt')
    Project(driver).close_stage(pass_name='Проект согласован вне Гермес. Инвестиции выделены',
                                next_stage='Ожидание реализации проекта', is_auto=True)
    FormB2CObjectOrder(driver).open_form(ComponentB2COrdersHierarchy(driver).get_customer_order_number())
    FormB2CObjectOrder(driver).add_contractor(discount=10, contractor='Саратовский', frame=555555)
    CustomerOrder(driver).open_order(FormB2CObjectOrder(driver).get_custom_order_order_id())
    CustomerOrder(driver).close_stage(pass_name="Положительно", next_stage="Подписание заказа (вне Гермес)",
                                      is_auto=True)
    ComponentNumberDSOFU(driver).add_DSOFU(kode=123456)
    CustomerOrder(driver).close_stage(pass_name="Положительно", next_stage="Создание ДС ОФУ (вне Гермес)", is_auto=True)
    CustomerOrder(driver).close_stage(pass_name="Положительно",
                                      next_stage="Формирование групповой КС-2 и их закрытие (вне Гермес)", is_auto=True)
    CustomerOrder(driver).close_stage(pass_name="Положительно", next_stage="Строительство завершено")
    Customer(driver).open_order(ComponentB2COrdersHierarchy(driver).get_customer_number())
    ComponentFiles(driver).add_file(name='Проектная документация (pdf)', type='Проектная документация (pdf)',
                                    file_name='file.txt')
    ComponentFiles(driver).add_file(name='Рабочая документация (pdf)', type='Рабочая документация (pdf)',
                                    file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Разработка ПД и РД")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Согласование ПД и РД")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Выполнение СМР/внесение статусов работ")
    ComponentFiles(driver).add_file(name='Протокол измерений ВОК', type='Протокол измерений ВОК', file_name='file.txt')
    ComponentFiles(driver).add_file(name='Таблица терминации (xls)', type='Таблица терминации (xls)',
                                    file_name='file.txt')
    ComponentFiles(driver).add_file(name='Схема организации связи', type='Схема организации связи',
                                    file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Приемка выполненных работ")
    ComponentFiles(driver).add_file(name='Ведомость ВО (pdf)', type='Ведомость ВО (pdf)', file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Пусконаладочные работы")
    ComponentFiles(driver).add_file(name='Квартирограмма', type='Квартирограмма', file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Приёмка минимального комплекта ИД")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Внесение в СЛТУ/предварительная готовность")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Разработка ИД")
    ComponentFiles(driver).add_file(name='Исполнительная документация', type='Исполнительная документация',
                                    file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Приёмка ИД")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Внесение данных в СЛТУ в статусе Готов")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Создание КС")
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Проверка и фиксация КС", is_auto=True)
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Подписание КС у Подрядчика", is_auto=True)
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Подписание КС в РТК")
    ComponentFiles(driver).add_file(name='КС-2 (скан pdf без штрих кода)', type='КС-2 (скан pdf без штрих кода)',
                                    file_name='file.txt')
    Customer(driver).close_stage(pass_name="Положительно", next_stage="Объект завершен")
    Project(driver).open_order(ComponentB2COrdersHierarchy(driver).get_project_number())
    Project(driver).check_current_stage('Проект реализован')
    assert True
