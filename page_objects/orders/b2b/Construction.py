from page_objects.orders.Order import Order
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentB2BOrdersHierarchy import ComponentB2BOrdersHierarchy
from page_objects.components.ComponentTypicalTechnicalSolutions import ComponentTypicalTechnicalSolutions
from page_objects.components.ComponentB2BChangeWorkPIRAndSMR import ComponentB2BChangeWorkPIRAndSMR
from page_objects.components.ComponentB2BTransferWorkHoz import ComponentB2BTransferWorkHoz


class Construction(Order):
    id = 3001
    name = 'Строительная заявка'

    ComponentCloseStage = ComponentCloseStage()
    ComponentB2BOrdersHierarchy = ComponentB2BOrdersHierarchy()
    ComponentTypicalTechnicalSolutions = ComponentTypicalTechnicalSolutions()
    ComponentB2BChangeWorkPIRAndSMR = ComponentB2BChangeWorkPIRAndSMR()
    ComponentB2BTransferWorkHoz = ComponentB2BTransferWorkHoz()
