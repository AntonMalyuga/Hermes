import pytest

from page_objects.reports.NonSynchronizedPricesReport import NonSynchronizedPricesReport
import testit


class TestNonSynchronizedPricesReport:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        NonSynchronizedPricesReport.open_by_default()
        assert NonSynchronizedPricesReport.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        NonSynchronizedPricesReport.open_by_default()
        assert NonSynchronizedPricesReport.get_name_report() == NonSynchronizedPricesReport.name
