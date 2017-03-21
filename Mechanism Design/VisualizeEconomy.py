from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.TextVisualization import TextData
from mesa.visualization.TextVisualization import TextVisualization

from WealthModel import WealthModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 6:
        portrayal["Color"] = "#5cd65c"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.6
    elif agent.wealth > 4:
        portrayal["Color"] = "#e6ffb3"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.4
    elif agent.wealth > 2:
        portrayal["Color"] = "#ffff99"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    elif agent.wealth > 0:
        portrayal["Color"] = "#ffcc99"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    else:
        portrayal["Color"] = "#ff884d"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.1
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
chart = ChartModule([
    {"Label": "Gini", "Color": "#6aa35e"}],
    data_collector_name='datacollector'
)

server = ModularServer(WealthModel, [grid, chart], "Wealth Model", 100, 10, 10)
server.port = 8521
server.launch()
