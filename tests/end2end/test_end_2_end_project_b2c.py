import time

from page_objects.b2cCreateConstructionProjectShow import B2CCreateConstructionProjectShow
from page_objects.orders.b2c.Project import Project
from page_objects.orders.b2c.b2cFormWorkVolume import B2cFormWorkVolume
from page_objects.orders.b2c.b2cFormSpecification import B2cFormSpecification
from page_objects.orders.b2c.ComponentControlDate import ComponentControlDate
from page_objects.orders.b2c.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.orders.b2c.ComponentCheckListWiFi import ComponentCheckListWiFi
from page_objects.orders.b2c.ComponentNaturalIndicators import ComponentNaturalIndicator
from page_objects.orders.b2c.ComponentAddictionalIncome import ComponentAdditionalIncome
from page_objects.orders.b2c.ComponentFiles import ComponentFiles
from page_objects.elements.UserLoginForm import UserLoginForm


def test_end_2_end_project_b2c(driver):

    works = {
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

    specifications = {
        'Wi-Fi оборудование 1': {
            'natural_indicator': 'Точки доступа'
        }
    }

    UserLoginForm(driver).autorization_default()
    driver.get('https://hermes-test.rt.ru/b2c/create_construction_project_show')
    B2CCreateConstructionProjectShow(driver).selected_rf('РФ Саратовский')
    B2CCreateConstructionProjectShow(driver).selected_is_need_broad('Нет')
    B2CCreateConstructionProjectShow(driver).selected_type_construct('Новостройка')
    B2CCreateConstructionProjectShow(driver).selected_customer_by_inn('111111111111')
    B2CCreateConstructionProjectShow(driver).enter_project_name('Автопрогон')
    B2CCreateConstructionProjectShow(driver).add_address('Саратов', 'Авиастроителей', 'д. 1')
    B2CCreateConstructionProjectShow(driver).enter_dh_for_address(120)
    B2CCreateConstructionProjectShow(driver).set_service_key('Wi-Fi')
    B2CCreateConstructionProjectShow(driver).enter_create_project()
    Project(driver).check_current_stage('Корректировка состава объектов проекта, проработка подключения услуг ключа на объектах и формирование предКП по ключу')
    ComponentCheckListWiFi(driver).add_cost_wifi(value='capex')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение лин. данных в ОТУ')
    Project(driver).open_form_work()
    B2cFormWorkVolume(driver).set_construct_method('Хоз.способ')
    B2cFormWorkVolume(driver).add_works(works)
    B2cFormWorkVolume(driver).close()
    Project(driver).open_form_specification()
    B2cFormSpecification(driver).set_construct_method('Хоз. способ')
    B2cFormSpecification(driver).add_specification(specifications)
    B2cFormSpecification(driver).close()
    Project(driver).close_stage(pass_name='Положительно', next_stage='Проработка ТР и внесение стоимости работ')
    ComponentCapitalCosts(driver).add_cost('привет мир', 300)
    ComponentNaturalIndicator(driver).add_random()
    Project(driver).close_stage(pass_name='Положительно', next_stage='Согласование состава оборудования услуг ключ в проекте')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Уточнение срока строительства и согласований')
    ComponentControlDate(driver).change_all_control_dates(30)
    Project(driver).close_stage(pass_name='Положительно', next_stage='Формирование КП и калькулятора')
    ComponentFiles(driver).add_file(name='КП Ключ', type='КП Ключ', file_name='file.txt')
    ComponentFiles(driver).add_file(name='Калькулятор Ключ', type='Калькулятор Ключ', file_name='file.txt')
    Project(driver).close_stage(pass_name='Положительно', next_stage='Формирование доходной части и согласование ТЭО')
    ComponentAdditionalIncome(driver).add_addictional_income(name='Вайфай', infrastructure_type='Wi-Fi', income_type='WiFi', abonent_type='Приростная', value=10000)
    time.sleep(20)
    assert True
