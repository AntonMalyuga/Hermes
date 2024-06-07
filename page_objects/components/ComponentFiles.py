import time
from dataclasses import dataclass
from pathlib import Path
from page import Page
from locator import Locator, Input, Select, CheckBox
import testit


@dataclass
class AddFile:
    file_type: str
    file_name: str
    file_link: str | None
    name_by_title: str | None
    file_version: str | None
    user_add_name: str | None
    date_add: str | None
    initiator: str | None
    bar_code: str | None = None
    kc: str | None = None


class ComponentFiles(Page):
    name = 'Вложения'

    _LOCATOR_GROUP = '//div[@class="panel panel-material"]//span[contains(., "Вложения")]'
    _FORM_ATTACHMENT = '//form[@action[contains(., "AddAttachment")]]'
    _LOCATOR_FORM_INPUT_FILE = f'{_FORM_ATTACHMENT}//input[contains(@name, "file")]'
    _LOCATOR_FORM_ATTACHMENT_TYPE = f'{_FORM_ATTACHMENT}//select[@id[contains(., "typeSelect")]]'
    _LOCATOR_FORM_ATTACHMENT_NAME = f'{_FORM_ATTACHMENT}//input[@id[contains(., "name")]]'
    _LOCATOR_FORM_ATTACHMENT_ADD_BUTTON = f'{_FORM_ATTACHMENT}//button[@type="submit"]'
    _LOCATOR_FORM_ATTACHMENT_VERSION = f'{_FORM_ATTACHMENT}//select[@name="versionedId"]'

    _LOCATOR_FORM_ATTACHMENT_DEL_BUTTON = '//button[contains(text(), "Удалить выбранные документы")]'
    _LOCATOR_FORM_ATTACHMENT_CONFIRM_DEL_BUTTON = '//button[contains(@form,"attachments_form") and contains(text(),"Подтвердить")]'

    _LOCATOR_TABLE_ADD_FILES = f'{_FORM_ATTACHMENT}/parent::div/parent::div//table//tbody'

    @classmethod
    def add_file(cls, name: str, type_file: str, file_name_in_path: str, name_file_version: str = None):
        with testit.step(f'Добавить файл с именем "{name}" и типом "{type_file}"'):
            cls.set_file_path(file_name_in_path)
            cls.set_file_type(type_file)
            cls.set_file_name(name)
            if name_file_version:
                time.sleep(1)
                cls.set_version_by_name(name_file_version)
            cls.submit()

    @classmethod
    def delete_all_files(cls):
        with testit.step(f'Удалить все вложения'):
            cnt_files = Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr').count
            for index_file in range(0, cnt_files):
                CheckBox(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{index_file + 1}]//input').checked()
            cls.click_delete_choose_documents()
            cls.click_confirm_delete_choose_documents()

    @classmethod
    def set_file_name(cls, name: str):
        with testit.step(f'Ввести имя файла "{name}"'):
            Input(cls._LOCATOR_FORM_ATTACHMENT_NAME).input(name)

    @classmethod
    def set_file_type(cls, type_file: str):
        with testit.step(f'Установить тип файла "{type_file}"'):
            Select(cls._LOCATOR_FORM_ATTACHMENT_TYPE).option(type_file)

    @classmethod
    def set_file_path(cls, file_name: str):
        with testit.step(f'Заполнить путь "{file_name}"'):
            file_path = str(Path(__file__).resolve().parents[2].joinpath('VO').joinpath(file_name))
            Input(cls._LOCATOR_FORM_INPUT_FILE).add_files(file_path)

    @classmethod
    def get_file_data(cls, xpath_position: str) -> AddFile:
        return AddFile(
            file_name=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[3]//a').text,
            file_type=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[2]/strong').text.strip(),
            file_link=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[3]//a').get_attribute('href'),
            name_by_title=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[3]//a').get_attribute(
                'title'),
            file_version=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[4]').text,
            user_add_name=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[5]').text,
            date_add=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[6]').text,
            initiator=Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[{xpath_position}]/td[7]').text
        )

    @classmethod
    def get_data_first_file(cls) -> AddFile:
        with testit.step(f'Получить данные по первому добавленному вложению'):
            return cls.get_file_data('1')

    @classmethod
    def get_data_last_file_by_name(cls, attachment_name: str) -> AddFile:
        with testit.step(f'Получить данные по последнему добавленному вложению с именем: {attachment_name}'):
            return cls.get_file_data(f'//tr[contains(., "{attachment_name}")][last()]')

    @classmethod
    def get_data_last_file_by_type(cls, attachment_type: str) -> AddFile:
        with testit.step(f'Получить данные по последнему добавленному вложению с типом: {attachment_type}'):
            return cls.get_file_data(f'//tr[contains(., "{attachment_type}")][last()]')

    @classmethod
    def get_data_first_file_by_type(cls, attachment_type: str) -> AddFile:
        with testit.step(f'Получить данные по первому добавленному вложению с типом: {attachment_type}'):
            return cls.get_file_data(f'//tr[contains(., "{attachment_type}")][1]')

    @classmethod
    def get_data_last_file(cls) -> AddFile:
        with testit.step(f'Получить данные по последнему добавленному вложению'):
            return cls.get_file_data('last()')

    @classmethod
    def get_cnt_add_files(cls) -> int:
        cnt = Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr').count
        with testit.step(f'Получить количество добавленных вложений: {cnt}'):
            return cnt

    @classmethod
    def get_cnt_add_files_by_type(cls, attachment_type: str) -> int:
        cnt = Locator(f'{cls._LOCATOR_TABLE_ADD_FILES}//tr[contains(., "{attachment_type}")]').count
        with testit.step(f'Получить количество добавленных вложений с типом {attachment_type}: {cnt}'):
            return cnt

    @classmethod
    def set_version_by_name(cls, file_nam: str):
        with testit.step(f'Добавить новую версию файла по имени: {file_nam}'):
            Locator(cls._LOCATOR_FORM_ATTACHMENT_VERSION).click()
            Select(cls._LOCATOR_FORM_ATTACHMENT_VERSION).option(file_nam)

    @classmethod
    def click_delete_choose_documents(cls):
        with testit.step(f'Нажать кнопку "Удалить выбранные документы"'):
            Locator(cls._LOCATOR_FORM_ATTACHMENT_DEL_BUTTON).click()

    @classmethod
    def click_confirm_delete_choose_documents(cls):
        with testit.step(f'Нажать кнопку "Подтвердить" для удаления выбранных документов'):
            Locator(cls._LOCATOR_FORM_ATTACHMENT_CONFIRM_DEL_BUTTON).click()

    @classmethod
    def submit(cls):
        with testit.step(f'Нажать кнопку "Добавить вложения"'):
            Locator(cls._LOCATOR_FORM_ATTACHMENT_ADD_BUTTON).click()
