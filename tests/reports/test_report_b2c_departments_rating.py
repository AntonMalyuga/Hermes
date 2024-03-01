import allure

from page_objects.reports.B2CDepartmentsRating import B2CDepartmentsRating
from page_objects.elements.UserLoginForm import UserLoginForm


@allure.feature('Отчёты')
@allure.step('Проверяет загруженность страницы формы отчёта')
def test_open_report_b2c_departments_rating(driver):
    B2CDepartmentsRating(driver).open()
    UserLoginForm(driver).autorization_default()
    assert B2CDepartmentsRating(driver).check_report()
