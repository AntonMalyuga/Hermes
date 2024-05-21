import pytest
import testit

from page_objects.reports.RerSubtask import RerSubtask


class TestRerSubtask:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        RerSubtask.open_by_default()
        assert RerSubtask.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        RerSubtask.open_by_default()
        assert RerSubtask.get_name_report() == RerSubtask.name
