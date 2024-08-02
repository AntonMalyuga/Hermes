from page_objects.orders.Order import Order
from page_objects.components.ComponentCloseStage import ComponentCloseStage
from page_objects.components.ComponentHistoryStages import ComponentHistoryStages
from page_objects.components.ComponentFiles import ComponentFiles
from page_objects.components.ComponentCapitalCosts import ComponentCapitalCosts
from page_objects.components.ComponentNaturalIndicators import ComponentNaturalIndicator
from page_objects.components.ComponentControlDate import ComponentControlDate
from page_objects.components.ComponentCheckListWiFi import ComponentCheckListWiFi
from page_objects.components.ComponentChangeSpecification import ComponentChangeSpecification
from page_objects.components.ComponentOpenPIRAndSMRForm import ComponentOpenPIRAndSMRForm


class Project(Order):
    id = 3049
    name = 'Строительный проект B2C'

    ComponentCloseStage = ComponentCloseStage()
    ComponentHistoryStages = ComponentHistoryStages()
    ComponentFiles = ComponentFiles()
    ComponentCapitalCosts = ComponentCapitalCosts()
    ComponentNaturalIndicator = ComponentNaturalIndicator()
    ComponentControlDate = ComponentControlDate()
    ComponentCheckListWiFi = ComponentCheckListWiFi()
    ComponentChangeSpecification = ComponentChangeSpecification()
    ComponentOpenPIRAndSMRForm = ComponentOpenPIRAndSMRForm()
