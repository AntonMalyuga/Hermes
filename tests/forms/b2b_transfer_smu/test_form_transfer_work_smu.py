import time

from page_objects.forms.FormB2BTransferWorkSMU import FormB2BTransferWorkSMU
import pytest
import testit


class TestComponentTransferWorkSMU:

    @testit.title(FormB2BTransferWorkSMU.name)
    @testit.displayName('Проверка переноса всех работ в схему СМУ из строительной заявки')
    @testit.description('Проверяется перенос всех работ в схему СМУ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):

        FormB2BTransferWorkSMU.open_form_by_order(order.id)

        if FormB2BTransferWorkSMU.check_is_all_work_smu():
            FormB2BTransferWorkSMU.set_all_works_construction_order()
            FormB2BTransferWorkSMU.save()
            FormB2BTransferWorkSMU.wait_reload_page()

        FormB2BTransferWorkSMU.set_all_works_smu()
        old_cnt = FormB2BTransferWorkSMU.get_cnt_all_work()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        new_cnt = FormB2BTransferWorkSMU.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkSMU.check_is_all_work_smu()


    @testit.title(FormB2BTransferWorkSMU.name)
    @testit.displayName('Проверка переноса всех работ из схемы СМУ в строительную заявку')
    @testit.description('Проверяется перенос всех работ из схемы СМУ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_order(self, order):
        FormB2BTransferWorkSMU.open_form_by_order(order.id)

        if not(FormB2BTransferWorkSMU.check_is_all_work_smu()):
            FormB2BTransferWorkSMU.set_all_works_smu()
            FormB2BTransferWorkSMU.save()
            FormB2BTransferWorkSMU.wait_reload_page()

        FormB2BTransferWorkSMU.set_all_works_construction_order()
        old_cnt = FormB2BTransferWorkSMU.get_cnt_all_work()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        new_cnt = FormB2BTransferWorkSMU.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkSMU.check_is_all_work_construction_order


    @testit.title(FormB2BTransferWorkSMU.name)
    @testit.displayName('Проверка счётчика переноса работ в схему СМУ из строительной заявки')
    @testit.description('Проверяется счётчик переноса работ в схему СМУ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):
        FormB2BTransferWorkSMU.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkSMU.get_cnt_all_work()

        if FormB2BTransferWorkSMU.check_is_all_work_smu():
            FormB2BTransferWorkSMU.set_all_works_construction_order()
            FormB2BTransferWorkSMU.save()
            FormB2BTransferWorkSMU.wait_reload_page()

        FormB2BTransferWorkSMU.set_all_works_smu()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkSMU.get_cnt_work_transfer_in_smu_by_alert()
        assert cnt_work == cnt_transfer_work

    @testit.title(FormB2BTransferWorkSMU.name)
    @testit.displayName('Проверка счётчика переноса работ из схемы СМУ в строительную заявку')
    @testit.description('Проверяется счётчик переноса работ из схемы СМУ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_and_check_alert(self, order):
        FormB2BTransferWorkSMU.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkSMU.get_cnt_all_work()


        if not(FormB2BTransferWorkSMU.check_is_all_work_smu()):
            FormB2BTransferWorkSMU.set_all_works_smu()
            FormB2BTransferWorkSMU.save()
            FormB2BTransferWorkSMU.wait_reload_page()

        FormB2BTransferWorkSMU.set_all_works_construction_order()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkSMU.get_cnt_work_transfer_in_smu_by_construction_order()
        assert cnt_work == cnt_transfer_work


    @testit.title(FormB2BTransferWorkSMU.name)
    @testit.displayName('Проверка создания заявки СМУ')
    @testit.description('Проверяется создание заявки СМУ с пустыми работами с последующем удалении заявки')
    @pytest.mark.smoke
    def test_create_smu(self, order_with_delete):
        FormB2BTransferWorkSMU.open_form_by_order(order_with_delete.id)
        FormB2BTransferWorkSMU.set_all_works_smu()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        smu_number = FormB2BTransferWorkSMU.get_number_create_order_smu()
        FormB2BTransferWorkSMU.set_all_works_construction_order()
        FormB2BTransferWorkSMU.save()
        FormB2BTransferWorkSMU.wait_reload_page()
        assert smu_number > 0