import pytest
from page_objects.reports.AggrClientProjectReport import AggrClientProjectReport
import testit


class TestAggrClientProjectReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        AggrClientProjectReport.open_by_default()
        assert AggrClientProjectReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        AggrClientProjectReport.open_by_default()
        assert AggrClientProjectReport.get_name_report() == AggrClientProjectReport.name
