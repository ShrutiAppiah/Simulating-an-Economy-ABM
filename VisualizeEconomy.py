import mesa

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
#from mesa.visualization.modules import TextElement
from mesa.visualization.ModularVisualization import ModularServer
#from mesa.visualization.TextVisualization import TextData
#from mesa.visualization.TextVisualization import TextVisualization

from WealthModel import WealthModel

economy_scale = 15
def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 1}

    """portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "w": 1,
                 "h": 1}"""

    """if agent.wealth > 6:
        portrayal["Color"] = "#5cd65c"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.6
        portrayal["w"] = 0.9
        portrayal["h"] = 0.9
    elif agent.wealth > 4:
        portrayal["Color"] = "#e6ffb3"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.4
        portrayal["w"] = 0.8
        portrayal["h"] = 0.8
    elif agent.wealth > 2:
        portrayal["Color"] = "#ffff99"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.3
        portrayal["w"] = 0.6
        portrayal["h"] = 0.6
    elif agent.wealth > 0:
        portrayal["Color"] = "#ffcc99"
        portrayal["Layer"] = 1
        #portrayal["r"] = 0.2
        portrayal["w"] = 0.3
        portrayal["h"] = 0.3
    elif agent.wealth == 0:
        portrayal["Color"] = "#ff884d"
        portrayal["Layer"] = 2
        #portrayal["r"] = 0.1
        portrayal["w"] = 0.1
        portrayal["h"] = 0.1
    elif agent.wealth < 0:
        portrayal["Color"] = "#4286f4"
        portrayal["Layer"] = 2
        #portrayal["r"] = 0.1
        portrayal["w"] = 0.1
        portrayal["h"] = 0.1
    else:
        portrayal["Color"] = "#f441f4"
        portrayal["Layer"] = 2
        #portrayal["r"] = 0.1
        portrayal["w"] = 0.1
        portrayal["h"] = 0.1"""
    if agent.wealth > 10:
        portrayal["Color"] = "#f441f4"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.8
    elif agent.wealth > 9:
        portrayal["Color"] = "#d966ff"
        portrayal["Layer"] = 0
        portrayal["r"] = 1
    elif agent.wealth > 8:
        portrayal["Color"] = "#8c66ff"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.9
    elif agent.wealth > 7:
        portrayal["Color"] = "#668cff"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.8
    elif agent.wealth > 6:
        portrayal["Color"] = "#66b3ff"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.7
    elif agent.wealth > 5:
        portrayal["Color"] = "#66d9ff"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.6
    elif agent.wealth > 4:
        portrayal["Color"] = "#66ffd9"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    elif agent.wealth > 3:
        portrayal["Color"] = "#66ff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.4
    elif agent.wealth > 2:
        portrayal["Color"] = "#b3ff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    elif agent.wealth > 1:
        portrayal["Color"] = "#ffff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.2
    elif agent.wealth > 0:
        portrayal["Color"] = "#ffd966"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.1
    else:
        portrayal["Color"] = "#ff8c66"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.0
    return portrayal

grid = CanvasGrid(agent_portrayal, economy_scale, economy_scale, 650, 650)
chart = ChartModule([
    {"Label": "Gini", "Color": "#6aa35e"}],
    data_collector_name='datacollector',
    canvas_height=600, canvas_width=550
)
#text = TextElement(js_code="document.write(5 + 6);")

server = ModularServer(WealthModel, [grid, chart], "Wealth Model", { "N" : economy_scale*economy_scale, "width" : economy_scale, "height" : economy_scale} )
server.port = 8521
server.launch()
