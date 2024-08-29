from page_objects.forms.FormB2BSpecification import FormB2BSpecification, Specification
import testit
import pytest


class TestFormB2BSpecification:

    @testit.title(FormB2BSpecification.name)
    @testit.displayName('Проверка добавления спецификации на форме редактирования оборудования')
    @testit.description('Проверяеся добавление новой работы на форме редактирования оборудования B2B')
    @pytest.mark.smoke
    def test_add_specification(self, order):
        FormB2BSpecification.open_form_by_order(order.id)
        FormB2BSpecification.delete_specification()
        FormB2BSpecification.add_specification(order.specification)
        FormB2BSpecification.wait_reload_page()
        assert order.specification.name == FormB2BSpecification.get_all_add_specifications()[0].name

    @testit.title(FormB2BSpecification.name)
    @testit.displayName('Проверка удаления спецификации на форме редактирования оборудования')
    @testit.description('Проверяеся удаление работы на форме редактирования оборудования B2B')
    @pytest.mark.smoke
    def test_delete_specification(self, order):
        FormB2BSpecification.open_form_by_order(order.id)
        FormB2BSpecification.add_specification(order.specification)
        FormB2BSpecification.wait_reload_page()
        FormB2BSpecification.delete_specification()
        FormB2BSpecification.wait_reload_page()
        assert FormB2BSpecification.get_cnt_add_specifications() == 0

    @testit.title(FormB2BSpecification.name)
    @testit.displayName('Проверка позиций добавляемого оборудования и новых существующих на спецификации')
    @testit.description(
        'Проверяется порядок таблиц добавляемых и новых работ, т.к. является частой багой после редактирования формы спецификации')
    @pytest.mark.smoke
    def test_check_position_table_elements_with_header_table(self, order):
        FormB2BSpecification.open_form_by_order(order.id)
        FormB2BSpecification.add_specification(order.specification)
        FormB2BSpecification.wait_reload_page()
        FormB2BSpecification.open_modal()
        FormB2BSpecification.show_specification_list_by_modal()
        FormB2BSpecification.add_specification_by_modal(order.specification.name)
        assert FormB2BSpecification.get_cnt_html_th_table() == FormB2BSpecification.get_cnt_html_td_by_first_add_specification()
        assert FormB2BSpecification.get_cnt_html_th_table() == FormB2BSpecification.get_cnt_html_td_by_first_new_specification()

    @testit.title(FormB2BSpecification.name)
    @testit.displayName('Проверка изменения параметров добавленного оборудования')
    @testit.description('Проверяется изменения различных параметров добавляемого оборудования на форме редактирования оборудования B2B')
    @pytest.mark.smoke
    def test_change_param_current_specification(self, order):
        FormB2BSpecification.open_form_by_order(order.id)
        FormB2BSpecification.delete_specification()
        FormB2BSpecification.add_specification(order.specification)
        FormB2BSpecification.wait_reload_page()
        change_specification = Specification(name=order.specification.name, cnt=12, fact_price=1200.12)
        FormB2BSpecification.set_fact_price_by_specification_name(change_specification)
        FormB2BSpecification.set_cnt_by_specification_name(change_specification)
        FormB2BSpecification.create_or_save_specification()
        FormB2BSpecification.wait_reload_page()
        current_specification = FormB2BSpecification.get_all_add_specifications()[0]
        assert current_specification.cnt == change_specification.cnt
        assert current_specification.fact_price == change_specification.fact_price
