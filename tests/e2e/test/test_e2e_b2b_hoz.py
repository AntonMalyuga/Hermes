import time

import pytest
import testit

from page_objects.components.ComponentTypicalTechnicalSolutions import ComponentTypicalTechnicalSolutions
from page_objects.forms.FormB2BCreateOldClientProject import FormB2BCreateOldClientProject
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentConnectionParameters import ComponentConnectionParameters
from page_objects.forms.FormB2BMapCreatePreTEOAndTEOOnMap import FormB2BMapCreatePreTEOAndTEOOnMap
from page_objects.components.ComponentRFPoint import ComponentRFPoint
from page_objects.components.ComponentRTPoint import ComponentRTPoint
from page_objects.components.ComponentBindingOT import ComponentBindingOT
from page_objects.components.ComponentCreatePreTEOAndTEOOnMap import ComponentCreatePreTEOAndTEOOnMap
from page_objects.components.ComponentB2BChangeWorkPIRAndSMR import ComponentB2BChangeWorkPIRAndSMR
from page_objects.components.ComponentB2BTransferWorkHoz import ComponentB2BTransferWorkHoz
from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz
from page_objects.forms.FormB2BWorkVolume import FormB2BWorkVolume
from page_objects.orders.b2b.Project import Project
from page_objects.components.ComponentProjectApproval import ComponentProjectApproval
from page_objects.orders.b2b.Client import Client
from page_objects.orders.b2b.Construction import Construction
from page_objects.components.ComponentB2BOrdersHierarchy import ComponentB2BOrdersHierarchy


@testit.workItemIds(1079)
@testit.title('E2E')
@testit.displayName('E2E B2B по строительству сети enternet')
@testit.description('E2E по строительству сети интернет с ТЭО и проработкой хоз. способа до конечного этапа')
@pytest.mark.slow
def test_e2e_b2b(driver):
    FormB2BCreateOldClientProject(driver).open()
    FormB2BCreateOldClientProject(driver).create_project_on_teo()
    FormB2BCreateOldClientProject(driver).open_created_client_order()
    Client(driver).close_not_current_tab()
    Client(driver).check_current_stage('Уточнение услуг ТЭО')
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Выбор варианта подключения')
    ComponentConnectionParameters(driver).change_connection_parameters(value='Оптика', coordination='Какое-то',
                                                                       conditions='Невероятные', crossing='Оптика',
                                                                       last_mile='Кроссировка', network='Сеть РТ')
    ComponentBindingOT(driver).change_binding_ot(
        value='АТС-VLG.ARGUS.1371454309, Область Саратовская, Город Саратов, проезд Соколовогорский 1-й, д. 13А')
    ComponentRFPoint(driver).change_rf_point(interface='CUSTOM', equipment='Кампуктеры')
    ComponentRTPoint(driver).change_rt_point(interface='CUSTOM', equipment='Какое-то')
    ComponentCreatePreTEOAndTEOOnMap(driver).open_form()
    FormB2BMapCreatePreTEOAndTEOOnMap(driver).create_pre_teo_and_teo()
    Construction(driver).close_not_current_tab()
    ComponentTypicalTechnicalSolutions(driver).set_typical_technical_solutions('не используется')
    ComponentB2BChangeWorkPIRAndSMR(driver).open_form_work()
    FormB2BWorkVolume(driver).fill_and_save_random_works()
    ComponentB2BTransferWorkHoz(driver).open_form_transfer_hoz_work()
    FormB2BTransferWorkHoz(driver).set_all_works_hoz()
    ComponentCloseStage(driver).close_stage(pass_name='Положительно (не требуется подготовка к СМР с УЗ)',
                                            next_stage='Согласование ТР с КБ (Уточнения намерений клиента)')

    project_order = ComponentB2BOrdersHierarchy(driver).get_project_number()
    client_order = ComponentB2BOrdersHierarchy(driver).get_client_number()
    hoz_order = ComponentB2BOrdersHierarchy(driver).get_hoz_number()

    Project(driver).open_order(project_order)
    Project(driver).check_current_stage(stage_name='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', second_do_reload=30)
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Ожидание подтверждения ТР в БТИ')
    Project(driver).reload_order()
    ComponentProjectApproval(driver).approval_osti_rf(is_approve=True, comment='lfdlkjdfslkjfdslkjds;lkj')
    ComponentProjectApproval(driver).approval_osti_kc(is_approve=True, comment='Привет МИР1!')
    ComponentProjectApproval(driver).approval_plan_kc(is_approve=True, comment='Привет ДАВФЛОдлвоыа!')
    Project(driver).check_current_stage('Проверка и отправка на согласование ТЭО ИП')
