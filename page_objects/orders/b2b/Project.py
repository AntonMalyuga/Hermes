from page_objects.orders.Order import Order
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentProjectGroup import ComponentProjectGroup


class Project(Order):
    id = 3003
    name = 'Клиентский проект'

    ComponentCloseStage = ComponentCloseStage()
    ComponentProjectGroup = ComponentProjectGroup()