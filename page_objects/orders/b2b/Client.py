from page_objects.orders.Order import Order
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentGeneralComment import ComponentGeneralComment
from page_objects.components.ComponentB2BOrdersHierarchy import ComponentB2BOrdersHierarchy
from page_objects.components.ComponentConnectionParameters import ComponentConnectionParameters
from page_objects.components.ComponentRFPoint import ComponentRFPoint
from page_objects.components.ComponentRTPoint import ComponentRTPoint
from page_objects.components.ComponentBindingOT import ComponentBindingOT
from page_objects.components.ComponentCreatePreTEOAndTEOOnMap import ComponentCreatePreTEOAndTEOOnMap


class Client(Order):
    id = 3000
    name = 'Клиентская заявка'

    ComponentCloseStage = ComponentCloseStage()
    ComponentGeneralComment = ComponentGeneralComment()
    ComponentB2BOrdersHierarchy = ComponentB2BOrdersHierarchy()
    ComponentConnectionParameters = ComponentConnectionParameters()
    ComponentBindingOT = ComponentBindingOT()
    ComponentRFPoint = ComponentRFPoint()
    ComponentRTPoint = ComponentRTPoint()
    ComponentCreatePreTEOAndTEOOnMap = ComponentCreatePreTEOAndTEOOnMap()
