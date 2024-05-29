from page_objects.orders.Order import Order
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentHistoryStages import ComponentHistoryStages


class Project(Order):
    id = 3049
    name = 'Строительный проект B2C'

    ComponentCloseStage = ComponentCloseStage()
    ComponentHistoryStages = ComponentHistoryStages()



