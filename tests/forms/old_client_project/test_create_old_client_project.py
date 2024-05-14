import time

import pytest
import testit
from page_objects.forms.FormB2BCreateOldClientProject import FormB2BCreateOldClientProject


@testit.title('Старая форма создания клиентского проекта')
@testit.displayName('Проверка заполнения наименования клиента')
@testit.description('Проверяется заполнение наименования клиента')
@pytest.mark.smoke
def test_set_client_name(driver):
    FormB2BCreateOldClientProject(driver).open()
    FormB2BCreateOldClientProject(driver).set_client_name('Привет МИР!')


@testit.title('Старая форма создания клиентского проекта')
@testit.displayName('Проверка срабатывания поиска клиента')
@testit.description('Проверяется срабатывания поиска существующего клиента')
@pytest.mark.smoke
def test_check_created_client_name_by_client_info(driver):
    FormB2BCreateOldClientProject(driver).open()
    FormB2BCreateOldClientProject(driver).set_client_name('ТЕСТ-ГЕРМЕС')
    FormB2BCreateOldClientProject(driver).set_client_inn('006165139943')
    FormB2BCreateOldClientProject(driver).set_client_kpp('616501001')
    time.sleep(1)
    FormB2BCreateOldClientProject(driver).update_client()
    time.sleep(5)
    x = FormB2BCreateOldClientProject(driver).get_info_created_clients()
    time.sleep(200)


