from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from WealthModel import WealthModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 4:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.6
    elif agent.wealth > 2:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.4
    elif agent.wealth > 0:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    else:
        portrayal["Color"] = "black"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.1
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
chart = ChartModule([
    {"Label": "Gini", "Color": "Black"}],
    data_collector_name='datacollector'
)

server = ModularServer(WealthModel, [grid, chart], "Wealth Model", 100, 10, 10)
server.port = 8521
server.launch()
