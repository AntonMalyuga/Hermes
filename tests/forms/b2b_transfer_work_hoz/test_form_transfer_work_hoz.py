import time

from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz
import pytest
import testit


class TestComponentTransferWorkHoz:

    @testit.title(FormB2BTransferWorkHoz.name)
    @testit.displayName('Проверка переноса всех работ в схему хоз. способ из строительной заявки')
    @testit.description('Проверяется перенос всех работ в схему хоз. способ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):
        FormB2BTransferWorkHoz.open_form_by_order(order.id)
        FormB2BTransferWorkHoz.set_all_works_hoz()
        old_cnt = FormB2BTransferWorkHoz.get_cnt_all_work()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        new_cnt = FormB2BTransferWorkHoz.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkHoz.check_is_all_work_hoz()


    @testit.title(FormB2BTransferWorkHoz.name)
    @testit.displayName('Проверка переноса всех работ из схемы хоз. способ в строительную заявку')
    @testit.description('Проверяется перенос всех работ из схемы хоз. способ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_order(self, order):
        FormB2BTransferWorkHoz.open_form_by_order(order.id)
        FormB2BTransferWorkHoz.set_all_works_construction_order()
        old_cnt = FormB2BTransferWorkHoz.get_cnt_all_work()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        new_cnt = FormB2BTransferWorkHoz.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkHoz.check_is_all_work_construction_order()


    @testit.title(FormB2BTransferWorkHoz.name)
    @testit.displayName('Проверка счётчика переноса работ в схему хоз. способ из строительной заявки')
    @testit.description('Проверяется счётчик переноса работ в схему хоз. способ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):
        FormB2BTransferWorkHoz.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkHoz.get_cnt_all_work()
        FormB2BTransferWorkHoz.set_all_works_construction_order()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        FormB2BTransferWorkHoz.set_all_works_hoz()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkHoz.get_cnt_work_transfer_in_hoz_by_alert()
        assert cnt_work == cnt_transfer_work

    @testit.title(FormB2BTransferWorkHoz.name)
    @testit.displayName('Проверка счётчика переноса работ из схемы хоз. способ в строительную заявку')
    @testit.description('Проверяется счётчик переноса работ из схемы хоз. способ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_and_check_alert(self, order):
        FormB2BTransferWorkHoz.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkHoz.get_cnt_all_work()
        FormB2BTransferWorkHoz.set_all_works_hoz()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        FormB2BTransferWorkHoz.set_all_works_construction_order()
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkHoz.get_cnt_work_transfer_in_hoz_by_construction_order()
        assert cnt_work == cnt_transfer_work


    @testit.title(FormB2BTransferWorkHoz.name)
    @testit.displayName('Проверка создания заявки хоз. способ')
    @testit.description('Проверяется создание заявки хоз. способ с пустыми работами с последующем удалении заявки')
    @pytest.mark.smoke
    def test_create_hoz(self, order_with_delete):
        FormB2BTransferWorkHoz.open_form_by_order(order_with_delete.id)
        FormB2BTransferWorkHoz.save()
        FormB2BTransferWorkHoz.wait_reload_page()
        assert FormB2BTransferWorkHoz.get_number_create_order_hoz() > 0