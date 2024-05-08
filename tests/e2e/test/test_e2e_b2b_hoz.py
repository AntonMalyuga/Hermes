import pytest
import testit
from page_objects.forms.CreateOldClientProject import CreateOldClientProject


@testit.workItemIds(1079)
@testit.title('E2E')
@testit.displayName('E2E B2B по строительству сети enternet')
@testit.description('E2E по строительству сети интернет с ТЭО и проработкой хоз. способа до конечного этапа')
@pytest.mark.smoke
def test_e2e_b2b(driver):
    CreateOldClientProject(driver).open()
    CreateOldClientProject(driver).create_project_on_teo()
