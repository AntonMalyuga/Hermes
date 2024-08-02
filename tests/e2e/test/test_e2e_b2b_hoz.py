import pytest
import testit

from page_objects.forms.FormB2BCreateOldClientProject import FormB2BCreateOldClientProject
from page_objects.forms.FormB2BMapCreatePreTEOAndTEOOnMap import FormB2BMapCreatePreTEOAndTEOOnMap
from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz
from page_objects.forms.FormB2BWorkVolume import FormB2BWorkVolume

from page_objects.orders.b2b.Project import Project
from page_objects.orders.b2b.Client import Client
from page_objects.orders.b2b.Construction import Construction


@testit.workItemIds(1079)
@testit.title('E2E')
@testit.displayName('E2E B2B по строительству сети enternet')
@testit.description('E2E по строительству сети интернет с ТЭО и проработкой хоз. способа до конечного этапа')
@pytest.mark.slow
def test_e2e_b2b():
    FormB2BCreateOldClientProject.open_by_default()
    FormB2BCreateOldClientProject.create_project_on_teo()
    FormB2BCreateOldClientProject.open_created_client_order()
    # Client.close_not_current_tab()
    # Client.check_current_stage('Уточнение услуг ТЭО')
    Client.ComponentCloseStage.close_stage(pass_name='Положительно', next_stage='Выбор варианта подключения')
    Client.ComponentConnectionParameters.change_connection_parameters(value='Оптика', coordination='Какое-то',
                                                                      conditions='Невероятные', crossing='Оптика',
                                                                      last_mile='Кроссировка', network='Сеть РТ')
    Client.ComponentBindingOT.change_binding_ot(
        value='АТС-VLG.ARGUS.1371454309, Область Саратовская, Город Саратов, проезд Соколовогорский 1-й, д. 13А')
    Client.ComponentRFPoint.change_rf_point(interface='CUSTOM', equipment='Кампуктеры')
    Client.ComponentRTPoint.change_rt_point(interface='CUSTOM', equipment='Какое-то')
    Client.ComponentCreatePreTEOAndTEOOnMap.open_form()
    # FormB2BMapCreatePreTEOAndTEOOnMap.create_pre_teo_and_teo()
    # Construction.close_not_current_tab()
    Construction.ComponentTypicalTechnicalSolutions.set_typical_technical_solutions('не используется')

    Construction.ComponentB2BChangeWorkPIRAndSMR.open_form_work()
    # FormB2BWorkVolume.fill_and_save_random_works()
    Construction.ComponentB2BTransferWorkHoz.open_form_transfer_hoz_work()
    FormB2BTransferWorkHoz.set_all_works_hoz()
    Construction.ComponentCloseStage.close_stage(pass_name='Положительно (не требуется подготовка к СМР с УЗ)',
                                                 next_stage='Согласование ТР с КБ (Уточнения намерений клиента)')

    project_order = Construction.ComponentB2BOrdersHierarchy.get_project_number()
    client_order = Construction.ComponentB2BOrdersHierarchy.get_client_number()
    hoz_order = Construction.ComponentB2BOrdersHierarchy.get_hoz_number()
    # Project.open_order(project_order)
    # Project.check_current_stage(stage_name='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', second_do_reload=30)
    Project.ComponentCloseStage.close_stage(pass_name='Положительно', next_stage='Ожидание подтверждения ТР в БТИ')
    # Project.reload_order()
    Project.ComponentProjectApproval.approval_osti_rf(is_approve=True, comment='lfdlkjdfslkjfdslkjds;lkj')
    Project.ComponentProjectApproval.approval_osti_kc(is_approve=True, comment='Привет МИР1!')
    Project.ComponentProjectApproval.approval_plan_kc(is_approve=True, comment='Привет ДАВФЛОдлвоыа!')
    # Project.check_current_stage('Проверка и отправка на согласование ТЭО ИП')
