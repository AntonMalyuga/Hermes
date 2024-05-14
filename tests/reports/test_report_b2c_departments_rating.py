from page_objects.reports.B2CDepartmentsRating import B2CDepartmentsRating
import testit


@testit.title('reports')
@testit.displayName('Проверить открытие отчёта "Рейтинг РФ по строительству B2C"')
@testit.description('Проверить открытие отчёта "Рейтинг РФ по строительству B2C"')
def test_open_report_b2c_departments_rating(driver):
    B2CDepartmentsRating(driver).open()
    assert B2CDepartmentsRating(driver).check_report()
