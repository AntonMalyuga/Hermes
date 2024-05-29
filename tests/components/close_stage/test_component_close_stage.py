import pytest
import testit

from page_objects.orders.b2c.Project import Project
from page_objects.orders.b2c.SMR import SMR


class TestComponentCloseStage:

    @testit.title('component')
    @testit.displayName('Проверить отображение информации о следующем этапе в умном переходе')
    @testit.description('Проверяется отображение информации о следующем этапе в умном переходе')
    @pytest.mark.smoke
    def test_show_name_next_stage_for_smart_pass(self, order_on_stage_development_technical_solution):
        Project.open_order(order_on_stage_development_technical_solution.id)
        Project.ComponentCloseStage.close_stage(pass_name='Положительно', is_go=False)
        assert Project.ComponentCloseStage.check_next_stage('Согласование состава оборудования услуг ключ в проекте')

    @testit.title('component')
    @testit.displayName('Проверить отображение информации о следующем этапе в обычном переходе')
    @testit.description('Проверяется отображение информации о следующем этапе в обычном переходе')
    @pytest.mark.smoke
    def test_show_name_next_stage_for_base_pass(self, order_on_stage_development_technical_solution):
        Project.open_order(order_on_stage_development_technical_solution.id)
        Project.ComponentCloseStage.close_stage(pass_name='Уточнение в ТУ', is_go=False)
        assert Project.ComponentCloseStage.check_next_stage('Уточнение лин. данных в ОТУ')

    @testit.title('component')
    @testit.displayName('Проверить отображение информации о следующем этапе в обратном переходе')
    @testit.description('Проверяется отображение информации о следующем этапе в обратном переходе')
    @pytest.mark.smoke
    def test_show_name_next_stage_for_back_pass(self, order_on_stage_clarification_in_grziuk):
        Project.open_order(order_on_stage_clarification_in_grziuk.id)
        Project.ComponentCloseStage.close_stage(pass_name='Уточнения предоставлены', is_go=False)
        assert Project.ComponentCloseStage.check_next_stage('Уточнение лин. данных в ОТУ')

    @testit.title('component')
    @testit.displayName('Проверить отображение ошибки при невыполненных условиях перехода')
    @testit.description('Проверяется отображение информации о следующем этапе в обратном переходе')
    @pytest.mark.smoke
    def test_show_name_next_stage_for_back_pass(self, order_on_stage_clarification_in_grziuk):
        Project.open_order(order_on_stage_clarification_in_grziuk.id)
        Project.ComponentCloseStage.close_stage(pass_name='Уточнения предоставлены', is_go=False)
        assert Project.ComponentCloseStage.check_show_alert_for_pass()

    @testit.title('component')
    @testit.displayName('Проверить закрытие этапа по кнопке Перейти')
    @testit.description('Проверяется функционал закрытие этапа по кнопке Перейти')
    @pytest.mark.smoke
    def test_base_close_stage(self, order_on_stage_correct_object_project_and_pre_teo):
        Project.open_order(order_on_stage_correct_object_project_and_pre_teo.id)
        Project.ComponentCloseStage.close_stage(pass_name='Положительно')
        Project.wait_reload_page()
        assert Project.get_current_stage() == 'Уточнение лин. данных в ОТУ'

    @testit.title('component')
    @testit.displayName('Проверить закрытие этапа по кнопке Перейти без проверок')
    @testit.description('Проверяется функционал закрытие этапа по кнопке Перейти без проверок')
    @pytest.mark.smoke
    def test_base_close_stage_without_require(self, order_on_stage_correct_object_project_and_pre_teo):
        Project.open_order(order_on_stage_correct_object_project_and_pre_teo.id)
        Project.ComponentCloseStage.close_stage(pass_name='Положительно', is_auto=True)
        Project.wait_reload_page()
        assert Project.get_current_stage() == 'Уточнение лин. данных в ОТУ'

    @testit.title('component')
    @testit.displayName('Проверить сохранения комментария после выполнения перехода')
    @testit.description('Проверяется сохранения комментария в истории прохождения заявки после выполненения перехода')
    @pytest.mark.smoke
    def test_save_comment_after_close_stage(self, order_on_stage_correct_object_project_and_pre_teo):
        Project.open_order(order_on_stage_correct_object_project_and_pre_teo.id)
        Project.ComponentCloseStage.close_stage(
            pass_name='Положительно',
            comment=order_on_stage_correct_object_project_and_pre_teo.comment
        )
        Project.wait_reload_page()
        current_comment = Project.ComponentHistoryStages.get_last_data_close_stage().comment
        need_comment = order_on_stage_correct_object_project_and_pre_teo.comment

        result: bool

        if current_comment.find(need_comment) != -1:
            result = True
        else:
            result = False

        assert result

    @testit.title('component')
    @testit.displayName('Проверить сохранения причины после выполнения перехода')
    @testit.description('Проверяется сохранения причины в истории прохождения заявки после выполненения перехода')
    @pytest.mark.smoke
    def test_save_reason_after_close_stage(self, order_on_stage_correct_object_project_and_pre_teo):
        Project.open_order(order_on_stage_correct_object_project_and_pre_teo.id)
        Project.ComponentCloseStage.close_stage(
            pass_name='Положительно',
            reason=order_on_stage_correct_object_project_and_pre_teo.reason
        )
        Project.wait_reload_page()

        need_reason = order_on_stage_correct_object_project_and_pre_teo.reason
        current_reason = Project.ComponentHistoryStages.get_last_data_close_stage().reason

        assert current_reason == need_reason

    @testit.title('component')
    @testit.displayName('Проверить движение заявки по сигналу СУС родитель - ребёнок')
    @testit.description('Проверяется движение заявки по сигналу СУС родитель - ребёнок')
    @pytest.mark.smoke
    def test_send_child_after_close_parent(self, order_on_stage_clarification_deadline):
        Project.open_order(order_on_stage_clarification_deadline.id)
        Project.ComponentCloseStage.close_stage(pass_name='Требуются уточнения',
                                                comment=order_on_stage_clarification_deadline.comment)
        Project.wait_reload_page()
        SMR.open_order(order_on_stage_clarification_deadline.child_id)
        SMR.get_current_stage()
        assert SMR.get_current_stage() == 'Ожидание проработки ТР'
