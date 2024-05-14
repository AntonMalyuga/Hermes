from page_objects.components.ComponentProjectApproval import ComponentProjectApproval
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.orders.b2b.Project import Project


def test_component_project_approval_all_approved(driver, order):
    Project(driver).open_order(order.id)
    Project(driver).check_current_stage(
        stage_name='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', second_do_reload=30)
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Ожидание подтверждения ТР в БТИ')
    Project(driver).reload_order()
    ComponentProjectApproval(driver).approval_osti_rf(is_approve=True, comment='lfdlkjdfslkjfdslkjds;lkj')
    ComponentProjectApproval(driver).approval_osti_kc(is_approve=True, comment='Привет МИР1!')
    ComponentProjectApproval(driver).approval_plan_kc(is_approve=True, comment='Привет ДАВФЛОдлвоыа!')
    Project(driver).check_current_stage('Проверка и отправка на согласование ТЭО ИП')
    ComponentCloseStage(driver).close_stage(pass_name='Отрицательно',
                                            next_stage='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', comment='Повторное согласование')


def test_component_project_approval_all_decline(driver, order):
    Project(driver).open_order(order.id)
    Project(driver).check_current_stage(
        stage_name='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', second_do_reload=30)
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Ожидание подтверждения ТР в БТИ')
    Project(driver).reload_order()
    ComponentProjectApproval(driver).approval_osti_rf(is_approve=False, comment='lfdlkjdfslkjfdslkjds;lkj')
    ComponentProjectApproval(driver).approval_osti_kc(is_approve=False, comment='Привет МИР1!')
    ComponentProjectApproval(driver).approval_plan_kc(is_approve=False, comment='Привет ДАВФЛОдлвоыа!')
    Project(driver).check_current_stage('Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)')


def test_component_project_approval_in_part_approved(driver, order):
    Project(driver).open_order(order.id)
    Project(driver).check_current_stage(
        stage_name='Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)', second_do_reload=30)
    ComponentCloseStage(driver).close_stage(pass_name='Положительно', next_stage='Ожидание подтверждения ТР в БТИ')
    Project(driver).reload_order()
    ComponentProjectApproval(driver).approval_osti_rf(is_approve=True, comment='lfdlkjdfslkjfdslkjds;lkj')
    ComponentProjectApproval(driver).approval_osti_kc(is_approve=False, comment='Привет МИР1!')
    ComponentProjectApproval(driver).approval_plan_kc(is_approve=True, comment='Привет ДАВФЛОдлвоыа!')
    Project(driver).check_current_stage('Согласование ТР с КБ по всему проекту (Уточнения намерений клиента)')