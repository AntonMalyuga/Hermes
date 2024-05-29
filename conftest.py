from driver import Driver


def is_mobile(request) -> bool:
    markers = request.node.own_markers
    if [mark for mark in markers if mark.name.lower() == 'mobile']:
        return True
    else:
        return False


def driver(request):
    mobile = is_mobile(request=request)
    webdriver = Driver(mobile=mobile)

    yield webdriver

    try:
        webdriver.quit()
    finally:
        webdriver.__class__._instances = {}
