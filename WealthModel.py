import random
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# %matplotlib notebook

from mesa import Agent, Model
from mesa.time import RandomActivation #RandomActivation is a simple scheduling style for activating agents
from mesa.space import MultiGrid

"""
class WealthAgent(Agent):
    #An agent with fixed initial wealth.
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        # Each agent begins with an allocated wealth
        self.wealth = 1
        
    def step(self):
        if self.wealth == 0:
            return
        other_agent = random.choice(self.model.schedule.agents)
        # Transaction - self's wealth transfers to other agent's wealth
        other_agent.wealth += 1
        self.wealth -= 1
        print('4')
        

class WealthModel(Model):
    #A model with some number of agents.
    def __init__(self, N):
        
        # N number of agents in the organization
        self.num_agents = N
        self.schedule = RandomActivation(self)
        print('j2')
        
        # Create agents
        for i in range(self.num_agents):
            a = WealthAgent(i, self)
            self.schedule.add(a) #Adds agents to the schedule
            #print("My Unique ID is:", unique_id)
            print('38j')
            
            # empty_model = WealthModel(10)
            # empty_model.step()
            # print('5')

            model = WealthModel(10)
            for i in range(10):
                  model.step() 
    
            agent_wealth = [a.wealth for a in model.schedule.agents]
            all_wealth = []
            for j in range(100):
                # Run the model
                model = WealthModel(10)
                for i in range(10):
                    model.step()
                    print('6')

                # Store the results
                for agent in model.schedule.agents:
                    all_wealth.append(agent.wealth)
                    
                    print('fndskjgd')
                    print("All wealth", all_wealth)
            
            #plt.figure()
            plt.plot(all_wealth, bins=range(max(all_wealth)+1))
            plt.hist(all_wealth, bins=range(max(all_wealth)+1))
            plt.show()
           
            """
class WealthModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = WealthAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()

class WealthAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            other.wealth += 2
            self.wealth -= 1

    def step(self):
        self.move()
        if self.wealth > 0:
            self.give_money()
            

            