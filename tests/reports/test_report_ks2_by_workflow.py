import pytest

from page_objects.reports.KS2ByWorkflow import KS2ByWorkflow
import testit


class TestKS2ByWorkflow:
    @testit.title('reports')
    @testit.displayName('Проверить открытие отчёта')
    @testit.description('Проверяется открытие отчёта')
    @pytest.mark.smoke
    def test_open_report(self):
        KS2ByWorkflow.open_by_default()
        assert KS2ByWorkflow.is_open_report()

    @testit.title('reports')
    @testit.displayName('Проверить наименование отчёта')
    @testit.description('Проверяется наименование отчёта')
    @pytest.mark.smoke
    def test_check_name(self):
        KS2ByWorkflow.open_by_default()
        assert KS2ByWorkflow.get_name_report() == KS2ByWorkflow.name
