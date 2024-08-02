import time

import pytest
import testit

from page_objects.orders.b2c.Project import Project


class TestComponentFiles:

    @testit.title('component')
    @testit.displayName('Проверить добавление вложения в заявку')
    @testit.description('Проверяется добавления вложения в заявку')
    @pytest.mark.smoke
    def test_add_attachment_in_order(self, order, attachment):
        Project.open_order(order.id)
        old_cnt_files = Project.ComponentFiles.get_cnt_add_files()
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path)
        Project.wait_reload_page()
        new_cnt_files = Project.ComponentFiles.get_cnt_add_files()
        assert old_cnt_files + 1 == new_cnt_files

    @testit.title('component')
    @testit.displayName('Проверить удаление вложения из заявки')
    @testit.description('Проверяется удаление вложений в заявке')
    @pytest.mark.smoke
    def test_delete_attachment_in_order(self, order, attachment):
        Project.open_order(order.id)
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path)
        Project.wait_reload_page()
        Project.ComponentFiles.delete_all_files()
        Project.wait_reload_page()
        assert Project.ComponentFiles.get_cnt_add_files() == 0

    @testit.title('component')
    @testit.displayName('Проверить удаление вложения с разными типами из заявки')
    @testit.description('Проверяется удаление вложений с разными типами в заявке')
    @pytest.mark.smoke
    def test_delete_diff_attachments_in_order(self, order, attachment_list):
        Project.open_order(order.id)
        for attachment in attachment_list:
            Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                            file_name_in_path=attachment.file_name_in_path)
            Project.wait_reload_page()
        Project.ComponentFiles.delete_all_files()
        Project.wait_reload_page()
        assert Project.ComponentFiles.get_cnt_add_files() == 0

    @testit.title('component')
    @testit.displayName('Проверить сохранение имени добавленного файла')
    @testit.description('Проверяется сохранение имени добавленного файла')
    @pytest.mark.smoke
    def test_save_name_add_attachment_in_order(self, order, attachment):
        Project.open_order(order.id)
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path)
        Project.wait_reload_page()
        data_add_file = Project.ComponentFiles.get_data_last_file_by_type(attachment.attachment_type)
        assert data_add_file.file_name == attachment.file_alternative_name

    @testit.title('component')
    @testit.displayName('Проверить сохранение внутреннего имени файла для скачивания')
    @testit.description('Проверяется сохранение внутреннего имени добавленного файла для скачивания')
    @pytest.mark.smoke
    def test_save_title_name_add_attachment_in_order(self, order, attachment):
        Project.open_order(order.id)
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path)
        Project.wait_reload_page()
        data_add_file = Project.ComponentFiles.get_data_last_file_by_type(attachment.attachment_type)
        assert data_add_file.name_by_title == attachment.file_name_in_path

    @testit.title('component')
    @testit.displayName('Проверить добавления новой версии файла')
    @testit.description('Проверяется добавления новой версии файла')
    @pytest.mark.smoke
    def test_add_attachment_with_version_in_order(self, order, attachment):
        Project.open_order(order.id)
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name, type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path)
        Project.wait_reload_page()
        Project.ComponentFiles.add_file(name=attachment.file_alternative_name,
                                        type_file=attachment.attachment_type,
                                        file_name_in_path=attachment.file_name_in_path,
                                        name_file_version=attachment.file_alternative_name)
        Project.wait_reload_page()
        assert Project.ComponentFiles.get_data_first_file_by_type(attachment.attachment_type).file_version == '2'

    @testit.title('component')
    @testit.displayName('Проверка отображения не обязательных вложений на заявке')
    @testit.description('Проверяется отображение не обязательных вложений на заявке')
    @pytest.mark.smoke
    def test_visible_need_attachment_in_order(self, order_with_need_attachment):
        Project.open_order(order_with_need_attachment.id)
        assert Project.ComponentFiles.check_is_need_attachments(order_with_need_attachment.need_attachment) > 0
