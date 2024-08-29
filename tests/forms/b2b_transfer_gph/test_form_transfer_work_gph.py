from page_objects.forms.FormB2BTransferWorkGPH import FormB2BTransferWorkGPH
import pytest
import testit


class TestComponentTransferWorkGPH:

    @testit.title(FormB2BTransferWorkGPH.name)
    @testit.displayName('Проверка переноса всех работ в схему ГПХ из строительной заявки')
    @testit.description('Проверяется перенос всех работ в схему ГПХ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):
        FormB2BTransferWorkGPH.open_form_by_order(order.id)
        FormB2BTransferWorkGPH.set_all_works_gph()
        old_cnt = FormB2BTransferWorkGPH.get_cnt_all_work()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        new_cnt = FormB2BTransferWorkGPH.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkGPH.check_is_all_work_gph()


    @testit.title(FormB2BTransferWorkGPH.name)
    @testit.displayName('Проверка переноса всех работ из схемы ГПХ в строительную заявку')
    @testit.description('Проверяется перенос всех работ из схемы ГПХ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_order(self, order):
        FormB2BTransferWorkGPH.open_form_by_order(order.id)
        FormB2BTransferWorkGPH.set_all_works_construction_order()
        old_cnt = FormB2BTransferWorkGPH.get_cnt_all_work()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        new_cnt = FormB2BTransferWorkGPH.get_cnt_all_work()
        assert old_cnt == new_cnt and FormB2BTransferWorkGPH.check_is_all_work_construction_order()


    @testit.title(FormB2BTransferWorkGPH.name)
    @testit.displayName('Проверка счётчика переноса работ в схему ГПХ из строительной заявки')
    @testit.description('Проверяется счётчик переноса работ в схему ГПХ из строительной заявки')
    @pytest.mark.smoke
    def test_transfer_work_in_hoz_and_check_alert(self, order):
        FormB2BTransferWorkGPH.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkGPH.get_cnt_all_work()
        FormB2BTransferWorkGPH.set_all_works_construction_order()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        FormB2BTransferWorkGPH.set_all_works_gph()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkGPH.get_cnt_work_transfer_in_gph_by_alert()
        assert cnt_work == cnt_transfer_work

    @testit.title(FormB2BTransferWorkGPH.name)
    @testit.displayName('Проверка счётчика переноса работ из схемы ГПХ в строительную заявку')
    @testit.description('Проверяется счётчик переноса работ из схемы ГПХ в строительную заявку')
    @pytest.mark.smoke
    def test_transfer_work_in_construction_and_check_alert(self, order):
        FormB2BTransferWorkGPH.open_form_by_order(order.id)
        cnt_work = FormB2BTransferWorkGPH.get_cnt_all_work()
        FormB2BTransferWorkGPH.set_all_works_gph()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        FormB2BTransferWorkGPH.set_all_works_construction_order()
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        cnt_transfer_work = FormB2BTransferWorkGPH.get_cnt_work_transfer_in_gph_by_construction_order()
        assert cnt_work == cnt_transfer_work


    @testit.title(FormB2BTransferWorkGPH.name)
    @testit.displayName('Проверка создания заявки ГПХ')
    @testit.description('Проверяется создание заявки ГПХ с пустыми работами с последующем удалении заявки')
    @pytest.mark.smoke
    def test_create_hoz(self, order_with_delete):
        FormB2BTransferWorkGPH.open_form_by_order(order_with_delete.id)
        FormB2BTransferWorkGPH.save()
        FormB2BTransferWorkGPH.wait_reload_page()
        assert FormB2BTransferWorkGPH.get_number_create_order_gph() > 0