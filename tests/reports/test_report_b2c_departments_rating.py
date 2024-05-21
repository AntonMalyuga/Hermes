import pytest

from page_objects.reports.B2CDepartmentsRating import B2CDepartmentsRating
import testit


class TestB2CDepartmentsRating:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        B2CDepartmentsRating.open_by_default()
        assert B2CDepartmentsRating.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        B2CDepartmentsRating.open_by_default()
        assert B2CDepartmentsRating.get_name_report() == B2CDepartmentsRating.name
