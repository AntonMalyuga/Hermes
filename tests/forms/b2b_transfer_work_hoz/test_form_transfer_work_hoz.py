from page_objects.forms.FormB2BTransferWorkHoz import FormB2BTransferWorkHoz
import pytest
import testit


@pytest.mark.usefixtures('form')
class TestComponentTransferWorkHoz:

    @testit.title('B2B: Выбор работ хоз. способом')
    @testit.displayName('Проверка переноса всех работ в схему хоз. способ из строительной заявки')
    @testit.description('Проверяется перенос всех работ в схему хоз. способ из строительной заявки')
    @pytest.mark.smoke
    def test_component_transfer_work_hoz(self, driver):
        FormB2BTransferWorkHoz(driver).set_all_works_hoz()

    @testit.title('B2B: Выбор работ хоз. способом')
    @testit.displayName('Проверка переноса всех работ из схемы хоз. способ в строительную заявку')
    @testit.description('Проверяется перенос всех работ из схемы хоз. способ в строительную заявку')
    @pytest.mark.smoke
    def test_component_transfer_work_hoz_2(self, driver):
        FormB2BTransferWorkHoz(driver).set_all_works_hoz()
