import pytest
import testit
from page_objects.orders.b2b.Project import Project


class TestComponentProjectGroup:

    @testit.title(Project.ComponentProjectGroup.name)
    @testit.displayName('Проверить список групп проекта')
    @testit.description('Проверить отображение списка групп проекта в редакторе групп проекта')
    @pytest.mark.smoke
    def test_list_project_group(self, order):
        Project.open_order(order.id)
        Project.ComponentProjectGroup.open_editor()
        Project.ComponentProjectGroup.wait_reload_page()
        assert  Project.ComponentProjectGroup.check_project_group_list()


    @testit.title(Project.ComponentProjectGroup.name)
    @testit.displayName('Проверить сохранение группы проекта')
    @testit.description('Проверить сохранение группы проекта при редактории группы')
    @pytest.mark.smoke
    def test_save_project_group(self, order):
        Project.open_order(order.id)
        Project.ComponentProjectGroup.open_editor()
        Project.ComponentProjectGroup.set_project_group(order.group_name)
        Project.ComponentProjectGroup.save_project_group()
        Project.wait_reload_page()
        assert  Project.ComponentProjectGroup.get_current_project_group() == order.group_name


    @testit.title(Project.ComponentProjectGroup.name)
    @testit.displayName('Проверить кнопку отмены изменения значения группы проекта')
    @testit.description('Проверяет работу кнопки отмены при изменении изменении группы проекта')
    @pytest.mark.smoke
    def test_cancel_changes_project_group(self, order):
        Project.open_order(order.id)
        do_group_name = Project.ComponentProjectGroup.get_current_project_group()
        Project.ComponentProjectGroup.open_editor()
        Project.ComponentProjectGroup.set_project_group(order.group_name)
        Project.ComponentProjectGroup.cansel_changes()
        Project.wait_reload_page()
        after_group_name = Project.ComponentProjectGroup.get_current_project_group()
        assert do_group_name == after_group_name