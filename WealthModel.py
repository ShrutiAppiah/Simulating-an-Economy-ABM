import random

from mesa import Agent, Model
from mesa.time import RandomActivation #RandomActivation is a simple scheduling style for activating agents

class WealthAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        # Each agent begins with an allocated wealth
        self.wealth = 1
        
        def step(self):
            # The agent's step will go here.
            pass

class WealthModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        
        # N number of agents in the organization
        self.num_agents = N
        self.schedule = RandomActivation(self)
        
        # Create agents
        for i in range(self.num_agents):
            a = WealthAgent(i, self)
            self.schedule.add(a) #Adds agents to the schedule
            print("My Unique ID is:", unique_id)
            
        def step(self):
            '''Advance the model by one step.'''
            self.schedule.step()
            print("My Unique ID is:", unique_id)
            
            # Tick = Time step. At every tick, agents have to perform an action.