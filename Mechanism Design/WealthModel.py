import random
import math

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
#from random import randint

treasury = 0

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return (1 + (1 / N) - 2 * B)


class WealthModel(Model):
    """A model with some number of agents."""

    def __init__(self, N, width, height):
        self.num_agents = N
        self.running = True
        self.grid = MultiGrid(height, width, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": lambda a: a.wealth}
        )
        # Create agents
        for i in range(self.num_agents):
            a = WealthAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n):
        for i in range(n):
            self.step()
            print("step = ", step())
            """tax_period = step()%10
            if tax_period == 0
                return_tax(self, treasury)"""
           
        
class WealthAgent(Agent):
    treasury = 0
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self, coins):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            other.wealth += coins
            self.wealth -= coins
            
    def donate_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        #print("self pos =", self.pos)
        #print("cellmates = ", cellmates)
        if len(cellmates) > 1:
            if self.wealth > 3:
                altruism = random.randint(0,1)
                if altruism == 0:
                    pass
                else:
                    other = random.choice(cellmates)
                    # If my neighbour's wealth is less than 40% of my wealth, I will donate an arbitrary sum of money to them
                    if other.wealth < 0.4*self.wealth:
                        max_donation = int(round(0.3*self.wealth)) 
                        donation = random.randint(0, max_donation)
                        other.wealth += donation
                        self.wealth -= donation
                        print("self wealth after donation = ", self.wealth)
                        print("neighbour's wealth after donation = ", other.wealth)
                        if other.wealth > self.wealth:
                            print("FAIL")
                    
    def take_tax(self):
        global treasury
        if self.wealth > 5:
            tax = math.floor(0.3*self.wealth)
            treasury += tax
            self.wealth -= tax
            print("I, MEMBER", self.pos, "HAVE BEEN TAXED UUGGGHHHHHHH, PAID", tax, "COINS!!!")
            print("TREASURY NOW =", treasury)
        
    #Reward agents        
    def project_reward(self, width, height):
        global treasury
        if treasury > 6:
            self.grid = MultiGrid(height, width, True)
            x = random.randint(0, self.grid.width-1)
            y = random.randint(0, self.grid.height-1) 
            a = self.model.grid.is_cell_empty([x,y])
            print("-------------------EMPTY = ", a)
            #receiver = cell(x,y)
            #receiver2 = __getitem__(x,y)
            #print("I AM A RECIEVER1", receiver)
            #print("I AM A RECIEVER2", receiver2)
            if a == False:
                receiver_position = (x,y)
                print("RECEIVER POSITION = ", receiver_position)
                receiver3 = self.model.grid.get_cell_list_contents(receiver_position)
                print("I AM A RECIEVER3", receiver3)

    def step(self):
        self.move()
        if self.wealth > 0:
            self.give_money(1)
            self.donate_money()
            self.take_tax()
            
            self.project_reward(10,10)
            #print("------------step------------")
            
         
            
