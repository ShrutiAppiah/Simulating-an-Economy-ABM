import random
import math

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

#Global variables
treasury = 0
economy_scale = 15

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return (1 + (1 / N) - 2 * B)


class WealthModel(Model):
    """A model with some number of agents."""
    global treasury
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

    ## Daily expenses
    # At every step, the agent makes a transaction with one of their neighbors
    def daily_transactions(self, coins):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            other.wealth += coins
            self.wealth -= coins
            
    ## Altruism
    # At every step, the agent makes a 50/50 choice of whether to donate money or not
    # If the agent chooses to donate, they donate 
    def donate_money(self):
        neighbours = self.model.grid.get_cell_list_contents([self.pos])
        #print("self pos =", self.pos)
        print("cellmates = ", neighbours)
        if len(neighbours) > 1:
            if self.wealth > 3:
                altruism = random.randint(0,1)
                if altruism == 0:
                    pass
                else:
                    for i in neighbours:
                        poor = random.choice(neighbours)
                        print("POOR = ", poor)
                        # If my neighbour's wealth is less than 40% of my wealth, 
                        # I will donate to them an arbitrary sum of money less than 30% of my wealth
                        if poor.wealth < 0.4*self.wealth:
                            print("Oh no, my neighbour is poor!", poor)
                            max_donation = int(round(0.3*self.wealth)) 
                            donation = random.randint(0, max_donation)
                            poor.wealth += donation
                            self.wealth -= donation
                            print("My wealth after donation = ", self.wealth)
                            print("Poor Neighbour's wealth after donation = ", poor.wealth)
                            break
                            
                        
    ## Taxes
    # At every step, the agent's wealth is checked.
    # If their wealth exceeds a certain amount, they are taxed 30% of their wealth.
    # Upon paying tax, the agent is admitted to the Committee and can post a public project 
    def collect_tax(self):
        global treasury
        if self.wealth > 9:
            tax = math.floor(0.3*self.wealth)
            treasury += tax
            self.wealth -= tax
            print("I, MEMBER", self.pos, "HAVE BEEN TAXED UUGGGHHHHHHH, PAID", tax, "COINS!!!")
            print("TREASURY NOW =", treasury)
        
   
    ## Reward agents
    # Agents who have participated in projects are rewarded with a bounty for completing the project
    # Bounty coins are taken from the Treasury
    def project_reward(self, width, height):
        global treasury
        if treasury > 6:
            self.grid = MultiGrid(height, width, True)
            x = random.randint(0, self.grid.width-1)
            y = random.randint(0, self.grid.height-1) 
            print("------EMPTY------- = ", self.model.grid.is_cell_empty([x,y]))
            
            if self.model.grid.is_cell_empty([x,y]) == False:
                position = (x,y)
                print("RECEIVER POSITION = ", position)
                potential_receivers = self.model.grid.get_cell_list_contents(position)
                receiver = random.choice(potential_receivers)
                print("BEFORE REWARD: I OWN THIS MUCH =", receiver.wealth)
                receiver.wealth += 2
                treasury -= 2
                print("AFTER REWARD: I OWN THIS MUCH =", receiver.wealth)

    def step(self):
        self.move()
        if self.wealth > 0:
            self.daily_transactions(1)
            self.donate_money()
            self.collect_tax()
            
            self.project_reward(economy_scale,economy_scale)
            #print("------------step------------")
            
         
            
