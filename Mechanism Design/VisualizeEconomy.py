from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.TextVisualization import TextData
from mesa.visualization.TextVisualization import TextVisualization

from WealthModel import WealthModel

economy_scale = 15
def agent_portrayal(agent):
    """portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.9}"""
    
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "w": 1,
                 "h": 1}

    if agent.wealth > 6:
        portrayal["Color"] = "#5cd65c"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.6
        portrayal["w"] = 0.6
        portrayal["h"] = 0.6
    elif agent.wealth > 4:
        portrayal["Color"] = "#e6ffb3"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.4
        portrayal["w"] = 0.4
        portrayal["h"] = 0.4
    elif agent.wealth > 2:
        portrayal["Color"] = "#ffff99"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.3
        portrayal["w"] = 0.3
        portrayal["h"] = 0.3
    elif agent.wealth > 0:
        portrayal["Color"] = "#ffcc99"
        portrayal["Layer"] = 1
        #portrayal["r"] = 0.2
        portrayal["w"] = 0.2
        portrayal["h"] = 0.2
    else:
        portrayal["Color"] = "#ff884d"
        portrayal["Layer"] = 2
        #portrayal["r"] = 0.1
        portrayal["w"] = 0.1
        portrayal["h"] = 0.1
    return portrayal

grid = CanvasGrid(agent_portrayal, economy_scale, economy_scale, 650, 650)
chart = ChartModule([
    {"Label": "Gini", "Color": "#6aa35e"}],
    data_collector_name='datacollector'
)

server = ModularServer(WealthModel, [grid, chart], "Wealth Model", economy_scale*economy_scale, economy_scale, economy_scale)
server.port = 8521
server.launch()
