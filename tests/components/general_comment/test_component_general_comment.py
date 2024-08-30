import pytest
import testit
from page_objects.orders.b2b.Client import Client


class TestComponentGeneralComment:

    @testit.title(Client.ComponentGeneralComment.name)
    @testit.displayName('Проверить сохранение комментария')
    @testit.description('Проверить сохранение комментария в заявке')
    @pytest.mark.smoke
    def test_save_project_group(self, order):
        Client.open_order(order.id)
        Client.ComponentGeneralComment.open_editor()
        Client.wait_reload_page()
        Client.ComponentGeneralComment.set_comment(order.comment)
        Client.ComponentGeneralComment.save_comment()
        Client.wait_reload_page()
        assert Client.ComponentGeneralComment.get_current_comment() == order.comment

    @testit.title(Client.ComponentGeneralComment.name)
    @testit.displayName('Проверить кнопку отмены изменения комментария')
    @testit.description('Проверяет работу кнопки отмены комментария в заявке')
    @pytest.mark.smoke
    def test_cancel_changes_project_group(self, order):
        Client.open_order(order.id)
        do_comment = Client.ComponentGeneralComment.get_current_comment()
        Client.ComponentGeneralComment.open_editor()
        Client.wait_reload_page()
        Client.ComponentGeneralComment.set_comment(order.comment)
        Client.ComponentGeneralComment.cancel_edit()
        Client.wait_reload_page()
        after_comment = Client.ComponentGeneralComment.get_current_comment()
        assert do_comment == after_comment


    @testit.title(Client.ComponentGeneralComment.name)
    @testit.displayName('Проверить максимальное количество символов в комментарии')
    @testit.description('Проверяет максимальное количество символов в комментарии до 2 тыс.')
    @pytest.mark.skip('HE-14390')
    def test_max_chars(self, order_with_max_comment):
        Client.open_order(order_with_max_comment.id)
        do_comment = Client.ComponentGeneralComment.get_current_comment()
        Client.ComponentGeneralComment.open_editor()
        Client.wait_reload_page()
        Client.ComponentGeneralComment.set_comment(order_with_max_comment.comment)
        Client.ComponentGeneralComment.cancel_edit()
        Client.wait_reload_page()
        after_comment = Client.ComponentGeneralComment.get_current_comment()
        assert do_comment == after_comment