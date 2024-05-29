import testit
import pytest
from page_objects.orders.b2c.Project import Project


class TestOrderData:
    @testit.title('interface_order')
    @testit.displayName('Проверить корректный номер заявки')
    @testit.description('Проверяется корректное отображение номера заявки в интерфейсе заявки')
    @pytest.mark.smoke
    def test_correct_number_order_id_on_interface_by_link(self, order_id):
        Project.open_order(order_id.id)
        assert Project.get_order_id() == order_id.id

    @testit.title('interface_order')
    @testit.displayName('Проверить корректный этап')
    @testit.description('Проверяется корректное отображение этапа в интерфесе заявки')
    @pytest.mark.smoke
    def test_correct_stage_name_on_interface_by_link(self, order_id):
        Project.open_order(order_id.id)
        assert Project.get_current_stage() == order_id.stage_name
