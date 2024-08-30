import time
from page import Page
from locator import Locator, Input, Select
from dataclasses import dataclass, field
import testit


@dataclass
class ProjectGroup:
    name: str


@dataclass
class ProjectGroups:
    @classmethod
    def get_groups(cls):
        return [
            "Миграция 2016",
            "Миграция 2017",
            "Миграция 2018",
            "Миграция 2019",
            "Миграция 2020",
            "Миграция 2021",
            "Миграция 2022",
            "Миграция 2023",
            "Миграция 2024",
            "Модернизация ОКН 2019",
            "Модернизация ОКН 2020",
            "Модернизация ОКН 2021",
            "Модернизация ОКН 2022",
            "Модернизация ОКН 2023",
            "Модернизация ОКН 2024",
            "Новая стройка ОКН 2019",
            "Новая стройка ОКН 2020",
            "Новая стройка ОКН 2021",
            "Новая стройка ОКН 2022",
            "Новая стройка ОКН 2023",
            "Новая стройка ОКН 2024",
            "ОКН Центр",
            "Пилотные заявки СЗ",
            "Спецпользователи",
            "Тендеры",
            "ФОИВ 2017"
        ]


class ComponentProjectGroup(Page):
    name = 'B2B: Группа проекта'

    _GROUP = '//div[@class="panel panel-material"]//span[contains(., "Общая информация")]/ancestor::div[2]'
    _LOCATOR_CURRENT_GROUP_NAME = f'{_GROUP}//div[./div[contains(text(), "Группа проекта")]]//span'
    _LOCATOR_BTN_OPEN_EDITOR = f'{_GROUP}//div[./div[contains(text(), "Группа проекта")]]//i'
    _LOCATOR_BTN_SAVE_PROJECT_GROUP = f'{_GROUP}//div[./div[contains(text(), "Группа проекта")]]//button'
    _LOCATOR_BTN_CANCEL_EDIT = f'{_GROUP}//div[./div[contains(text(), "Группа проекта")]]//a[./span]'
    _LOCATOR_SELECT_PROJECT_GROUP = f'{_GROUP}//div[./div[contains(text(), "Группа проекта")]]//select'

    @classmethod
    def get_current_project_group(cls) -> str:
        group_name = Locator(cls._LOCATOR_CURRENT_GROUP_NAME).text
        with testit.step(f'Получить текущее имя группы проекта {group_name}'):
            return group_name

    @classmethod
    def open_editor(cls):
        with testit.step('Открыть редактор группы проекта'):
            Locator(cls._LOCATOR_BTN_OPEN_EDITOR).click()

    @classmethod
    def set_project_group(cls, group_name: str):
        with testit.step(f'Изменить группу проекта на {group_name}'):
            cls.wait_reload_page()
            text_with_index = Locator(f'//option[contains(text(), "{group_name}")]').text
            Select(cls._LOCATOR_SELECT_PROJECT_GROUP).option(text_with_index)

    @classmethod
    def get_project_group_list(cls) -> list[str]:
        with testit.step('Получить список групп проекта'):
            group_list = []
            html_group_list = Locator(f'{cls._LOCATOR_SELECT_PROJECT_GROUP}//option').all

            for group_name in html_group_list:

                group_name = ''.join(group_name.all_text_contents()).strip().rsplit(': ', 1)

                if group_name[0] not in ('Выберите группу клиентского проекта', 'Без группы'):
                    group_list.append(group_name[1])

            return group_list

    @classmethod
    def save_project_group(cls):
        with testit.step('Сохранить изменения группы проекта'):
            Locator(cls._LOCATOR_BTN_SAVE_PROJECT_GROUP).click()

    @classmethod
    def cansel_changes(cls):
        with testit.step('Отменить изменения группы проекта'):
            Locator(cls._LOCATOR_BTN_CANCEL_EDIT).click()

    @classmethod
    def check_project_group_list(cls) -> bool:
        with testit.step('Проверить список групп проекта'):
            return ProjectGroups.get_groups() == cls.get_project_group_list()
