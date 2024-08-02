import time

from page_objects.forms.FormB2BWorkVolume import FormB2BWorkVolume


class TestFormB2BWorkVolume:
    def test_form_b2b_work(self, order):
        FormB2BWorkVolume.open_form(order.id)
        time.sleep(4)
        FormB2BWorkVolume.delete_all_works()
        time.sleep(30)
