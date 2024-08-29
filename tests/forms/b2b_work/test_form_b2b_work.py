import time
from page_objects.forms.FormB2BWorkVolume import FormB2BWorkVolume, ClusterMethods
import testit
import pytest


class TestFormB2BWorkVolume:

    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка добавления работ в форме редактирования ПИР/СМР')
    @testit.description('Проверяется добавление новых работ в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_add_work_after_save(self, order):
        FormB2BWorkVolume.open_form(order.id)
        FormB2BWorkVolume.delete_all_works()
        FormB2BWorkVolume.click_show_all_works()
        FormB2BWorkVolume.add_work(work=order.work)
        FormB2BWorkVolume.save_works()
        FormB2BWorkVolume.open_form(order.id)
        assert FormB2BWorkVolume.get_html_add_works()[0].name == order.work.name
        assert FormB2BWorkVolume.get_html_add_works()[0].cnt == order.work.count
        assert FormB2BWorkVolume.get_html_add_works()[0].type == order.work.work_type

    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка удаления работ в форме редактирования ПИР/СМР')
    @testit.description('Проверяется удаления работ в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_delete_work_after_save(self, order):
        FormB2BWorkVolume.open_form(order.id)
        FormB2BWorkVolume.click_show_all_works()
        FormB2BWorkVolume.add_work(work=order.work)
        FormB2BWorkVolume.save_works()
        FormB2BWorkVolume.open_form(order.id)
        assert len(FormB2BWorkVolume.get_html_add_works()) == 0

    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка смены рамки в форме редактирования ПИР/СМР')
    @testit.description('Провеется изменение рамки в форме редактирования в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_change_calculator(self, order):
        FormB2BWorkVolume.open_form(order.id)
        FormB2BWorkVolume.change_calculator_frame('Глобальный Калькулятор B2B КЦ 2023')
        FormB2BWorkVolume.wait_reload_page()
        assert FormB2BWorkVolume.get_current_name_calculator_frame() == 'Глобальный Калькулятор B2B КЦ 2023'
        FormB2BWorkVolume.change_calculator_frame('Глобальный Калькулятор B2B КЦ 2022')
        FormB2BWorkVolume.wait_reload_page()
        assert FormB2BWorkVolume.get_current_name_calculator_frame() == 'Глобальный Калькулятор B2B КЦ 2022'

    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка изменения количества работ в форме редактирования ПИР/СМР')
    @testit.description(
        'Проверяется изменение количество работ на уже добавленной работе в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_change_calculator(self, order):
        FormB2BWorkVolume.open_form(order.id)
        FormB2BWorkVolume.delete_all_works()
        FormB2BWorkVolume.click_show_all_works()
        FormB2BWorkVolume.add_work(work=order.work)
        FormB2BWorkVolume.save_works()
        FormB2BWorkVolume.wait_reload_page()
        FormB2BWorkVolume.change_cnt_work_by_add_work(order.work, 23)
        FormB2BWorkVolume.save_works()
        FormB2BWorkVolume.open_form(order.id)
        assert FormB2BWorkVolume.get_html_add_works()[0].cnt == 23


    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка отображения списка работ в форме редактирования ПИР/СМР')
    @testit.description('Проверяется загрузка всех работ на рамке в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_change_calculator(self, order):
        FormB2BWorkVolume.open_form(order.id)
        FormB2BWorkVolume.delete_all_works()
        FormB2BWorkVolume.click_show_all_works()
        assert FormB2BWorkVolume.get_cnt_visible_works() == 1137


    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка отображения списка работ в форме редактирования ПИР/СМР')
    @testit.description('Проверяется загрузка всех работ на рамке в форме редактирования ПИР/СМР')
    @pytest.mark.smoke
    def test_change_calculator(self, order_with_cluster):
        FormB2BWorkVolume.open_form(order_with_cluster.id)
        FormB2BWorkVolume.delete_all_works()
        FormB2BWorkVolume.click_show_all_works()
        assert FormB2BWorkVolume.get_cnt_visible_works() == 1137



    @testit.title(FormB2BWorkVolume.name)
    @testit.displayName('Проверка редактирования масштабных работ в форме редактирования ПИР/СМР')
    @testit.description('Проверяется изменение масштабных работ в форме редактирования ПИР/СМР')
    @pytest.mark.skip(reason='HE-14355')
    def test_change_clusters(self, order_with_cluster):
        FormB2BWorkVolume.open_form(order_with_cluster.id)
        cluster_methods = ClusterMethods(
            change_line_type='По существующим опорам',
            # change_cable_type='Существующий 24',
            change_change_support_type=1,
            change_line_length=2,
            change_well_installation=3,
            change_gnb_group_1_3=4,
            change_gnb_group_4_6=5,
            change_installation_of_wooden_supports=6,
            change_installation_of_reinforced_concrete_supports=7,
            change_installation_of_metal_supports=8,
            change_cable_entry_device=9,
            change_insert_cable_channel=10,
            change_recovery_cable_channel=11,
            change_create_cable_chanel=12
        )
        FormB2BWorkVolume.change_cluster_parameters_by_row(0, cluster_methods)
        time.sleep(14)
