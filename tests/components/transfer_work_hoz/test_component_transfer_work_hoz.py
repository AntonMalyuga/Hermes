import testit
import pytest

from page_objects.orders.b2b.Construction import Construction


class TestFormB2BSpecification:

    @testit.title(Construction.ComponentB2BTransferWorkHoz.name)
    @testit.displayName('Проверка добавления спецификации на форме редактирования оборудования')
    @testit.description('Проверяеся добавление новой работы на форме редактирования оборудования B2B')
    @pytest.mark.smoke
    def test_add_specification(self, order):
        Construction.ComponentB2BTransferWorkHoz.open_form_by_order(order.id)
        FormB2BSpecification.delete_specification()
        FormB2BSpecification.add_specification(order.specification)
        FormB2BSpecification.wait_reload_page()
        assert order.specification.name == FormB2BSpecification.get_all_add_specifications()[0].name