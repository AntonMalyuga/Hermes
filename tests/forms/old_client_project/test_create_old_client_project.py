import time

import pytest
import testit
from page_objects.forms.FormB2BCreateOldClientProject import FormB2BCreateOldClientProject
from page_objects.orders.b2b.Project import Project
from page_objects.orders.b2b.Client import Client


class TestFormB2BCreateOldClientProject:
    @testit.title('form')
    @testit.displayName('Проверить этапы клиентского проекта и клиентской заявки после создания на ТЭО')
    @testit.description('Проверяются этапы клиентского проекта и клиентской заявки после создания на ТЭО')
    @pytest.mark.smoke
    def test_create_project_on_teo(self, project_on_teo):
        FormB2BCreateOldClientProject.open_by_default()
        FormB2BCreateOldClientProject.create_project(project=project_on_teo)
        FormB2BCreateOldClientProject.wait_reload_page()
        project_order_id = FormB2BCreateOldClientProject.get_created_client_project_order()
        client_order_id = FormB2BCreateOldClientProject.get_created_client_order()
        Project.open_order(project_order_id)
        result_project = Project.check_current_stage('Уточнение услуг ТЭО')
        Client.open_order(client_order_id)
        result_client = Client.check_current_stage('Уточнение услуг ТЭО')
        assert result_client and result_project

    @testit.title('form')
    @testit.displayName('Проверить этапы клиентского проекта и клиентской заявки после создания на ПредТЭО')
    @testit.description('Проверяются этапы клиентского проекта и клиентской заявки после создания на ПредТЭО')
    @pytest.mark.smoke
    def test_create_project_on_pre_teo(self, project_on_pre_teo):
        FormB2BCreateOldClientProject.open_by_default()
        FormB2BCreateOldClientProject.create_project(project=project_on_pre_teo)
        FormB2BCreateOldClientProject.wait_reload_page()
        project_order_id = FormB2BCreateOldClientProject.get_created_client_project_order()
        client_order_id = FormB2BCreateOldClientProject.get_created_client_order()
        Project.open_order(project_order_id)
        result_project = Project.check_current_stage('Уточнение услуг ПредТЭО')
        Client.open_order(client_order_id)
        result_client = Client.check_current_stage('Уточнение услуг ПредТЭО')
        assert result_client and result_project

    @testit.title('form')
    @testit.displayName('Проверить этапы клиентского проекта и клиентской заявки после создания на ТЭО с ТВП')
    @testit.description('Проверяются этапы клиентского проекта и клиентской заявки после создания на ТЭО с ТВП')
    @pytest.mark.smoke
    def test_create_project_on_teo_and_tvp(self, project_on_teo_and_tvp):
        FormB2BCreateOldClientProject.open_by_default()
        FormB2BCreateOldClientProject.create_project(project=project_on_teo_and_tvp)
        FormB2BCreateOldClientProject.wait_reload_page()
        project_order_id = FormB2BCreateOldClientProject.get_created_client_project_order()
        client_order_id = FormB2BCreateOldClientProject.get_created_client_order()
        Project.open_order(project_order_id)
        result_project = Project.check_current_stage('Уточнение услуг ТЭО')
        Client.open_order(client_order_id)
        result_client = Client.check_current_stage('Строительство не требуется (есть ТВП)')
        assert result_client and result_project

    @testit.title('form')
    @testit.displayName('Проверить этапы клиентского проекта и клиентской заявки после создания на ПредТЭО с ТВП')
    @testit.description('Проверяются этапы клиентского проекта и клиентской заявки после создания на ПредТЭО с ТВП')
    @pytest.mark.smoke
    def test_create_project_on_pre_teo_and_tvp(self, project_on_pre_teo_and_tvp):
        FormB2BCreateOldClientProject.open_by_default()
        FormB2BCreateOldClientProject.create_project(project=project_on_pre_teo_and_tvp)
        FormB2BCreateOldClientProject.wait_reload_page()
        project_order_id = FormB2BCreateOldClientProject.get_created_client_project_order()
        client_order_id = FormB2BCreateOldClientProject.get_created_client_order()
        Project.open_order(project_order_id)
        result_project = Project.check_current_stage('Уточнение услуг ПредТЭО')
        Client.open_order(client_order_id)
        result_client = Client.check_current_stage('Строительство не требуется (есть ТВП)')
        assert result_client and result_project
